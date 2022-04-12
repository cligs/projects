package de.uniwue.ds.dsdetection.featuregens;

import java.util.ArrayList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class PuctMarkSentenceFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		String[] returnv = new String[] { "PUNCQ=FALSE", "PUNCE=FALSE", "PUNCC=FALSE",
				"PUNCD=FALSE" };
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			returnv = new String[] { "FALSE", "FALSE", "FALSE", "FALSE" };

		for (AnnotationFS anno : covered) {
			if (anno.getCoveredText().equals("?"))
				if (DSDetectionFeatureGenerators.CSVFORMAT)
					returnv[0] = "TRUE";
				else
					returnv[0] = "PUNCQ=TRUE";
			if (anno.getCoveredText().equals("!"))
				if (DSDetectionFeatureGenerators.CSVFORMAT)
					returnv[1] = "TRUE";
				else
					returnv[1] = "PUNCE=TRUE";
			if (anno.getCoveredText().equals(":"))
				if (DSDetectionFeatureGenerators.CSVFORMAT)
					returnv[2] = "TRUE";
				else
					returnv[2] = "PUNCC=TRUE";
			if (anno.getCoveredText().equals("."))
				if (DSDetectionFeatureGenerators.CSVFORMAT)
					returnv[3] = "TRUE";
				else
					returnv[3] = "PUNCD=TRUE";
		}
		return returnv;
	}

}
