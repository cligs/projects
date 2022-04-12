package de.uniwue.ds.dsdetection.featuregens;

import java.util.ArrayList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class AusrufFeatureGenerator extends AKallimachosStandardFeatureGenerator {
	// Todo: Use HashSet
	private static boolean LIST_VALUES = false;

	public final static String[] AUSRUFE = new String[] {
			// "ah", "oh", "hé", "hein", "hélas", "bah", "holà", "hem", "chut",
			// "bravo", "eh", "euh", "fi", "hep", "ouf", "ouste"
			"ah", "oh", "hey", "eh", "bah", "bravo", "he", "uh", "ei", "potzblitz", "huch", "oha", "echt", "heureka",
			"holla", "wow", "igitt", "pfui", "bäh", "hurra", "halleluja", "juhu",  "hm", "voila", "hehe", "ach",
			"hopp", "zack", "obacht", "vorsicht", "hurra", "ups" };

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		String[] returnv = new String[AUSRUFE.length];
		for (int i = 0; i < returnv.length; i++)
			if (DSDetectionFeatureGenerators.CSVFORMAT)
				returnv[i] = "FALSE";
			else {
				returnv[i] = "INTERJECTION_" + AUSRUFE[i].toUpperCase() + "=FALSE";
			}

		for (AnnotationFS anno : covered) {
			for (int i = 0; i < returnv.length; i++) {
				if (anno.getCoveredText().toLowerCase().equals(AUSRUFE[i]))
					if (DSDetectionFeatureGenerators.CSVFORMAT)
						returnv[i] = "TRUE";
					else {
						if (LIST_VALUES)
							returnv[i] = "INTERJECTION_" + AUSRUFE[i].toUpperCase() + "=TRUE";
						else {
							return new String[] { "INTERJECTION=TRUE" };
						}

					}
			}
		}
		if (!LIST_VALUES) {
			return new String[] { "INTERJECTION=FALSE" };
		}
		return returnv;
	}

}
