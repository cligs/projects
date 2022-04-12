package de.uniwue.ds.dsdetection.featuregens;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class SubclauseLengthFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		LinkedList<Integer> subclalengths = new LinkedList<Integer>();
		int currentSubclLength = 0;
		for (AnnotationFS anno : covered) {
			if (anno.getCoveredText().equals(",")) {
				subclalengths.add(currentSubclLength);
				currentSubclLength = 0;
			} else
				currentSubclLength++;
		}
		double[] arr = new double[subclalengths.size()];
		for (int i = 0; i < subclalengths.size(); i++)
			arr[i] = subclalengths.get(i);

		// Collections.sort(subclalengths);
		int big = 5;
		int small = 3;

		if (arr.length < 2) {
			if (DSDetectionFeatureGenerators.CSVFORMAT)
				return new String[] { "FALSE" };
			else
				return new String[] { "INSUBC=FALSE" };
		} else {
			for (int i = 0; i < arr.length; i++) {
				if (i - 1 >= 0 && arr[i - 1] < big) // prev segment too small
					continue;
				if (i + 1 < arr.length && arr[i + 1] < big)
					continue; // next segment too small
				if (arr[i] < small)
					if (DSDetectionFeatureGenerators.CSVFORMAT)
						return new String[] { "TRUE" };
					else
						return new String[] { "INSUBC=TRUE" };
			}
		}
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			return new String[] { "FALSE" };
		else
			return new String[] { "INSUBC=FALSE" };

		// if (arr.length <= 1)
		// return new String[] {"SUBCLAUSELENGTH_SORTED=NaN"};
		//// return new String[] {"SUBCLAUSELENGTH_SORTED=" +
		// (subclalengths.get(0) * 1.0 / subclalengths.get(1))};
		// return new String[] {"SUBCLAUSELENGTH_SORTED=" +
		// ((int)(Math.log10(getVariance(arr) * 10)*10)<5?"TRUE":"FALSE")};
	}

	double getMean(double[] data) {
		double sum = 0.0;
		for (double a : data)
			sum += a;
		return sum / data.length;
	}

	double getVariance(double[] data) {
		double mean = getMean(data);
		double temp = 0;
		for (double a : data)
			temp += (mean - a) * (mean - a);
		return temp / data.length;
	}

}
