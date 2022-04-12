package de.uniwue.ds.dsdetection.featuregens;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class CommaCountFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		int commas = 0;
		for (AnnotationFS anno : covered) {
			if (anno.getCoveredText().equals(","))
				commas++;
		}
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			return new String[] { "" + commas };
		else
			return new String[] { "COMMAS=" + commas };
	}

}
