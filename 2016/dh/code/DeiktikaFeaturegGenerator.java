package de.uniwue.ds.dsdetection.featuregens;

import java.util.ArrayList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class DeiktikaFeaturegGenerator extends AKallimachosStandardFeatureGenerator {

	// Todo: Use HashSet
	public final static String[] DEIKTIKA = new String[] { 
			//"ici", "là-bas", "hier", "aujourd'hui", "demain", "maintenant"
			"hier", "dahin", "dahinten", "dort", "dorthin", "da", "gestern", "heute", "vorgestern", "morgen", "übermorgen", "jetzt", "dieser"
			};

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		String[] returnv = new String[DEIKTIKA.length];
		for (int i = 0; i < returnv.length; i++)
			returnv[i] = "DEIKTIKA_" + DEIKTIKA[i].toUpperCase() + "=FALSE";

		for (AnnotationFS anno : covered) {
			for (int i = 0; i < returnv.length; i++) {
				if (anno.getCoveredText().toLowerCase().equals(DEIKTIKA[i])) {
					if (DSDetectionFeatureGenerators.CSVFORMAT)
						return new String[] { "TRUE" };
					else
						return new String[] { "DEIKTIKA=TRUE" };
				}
			}
		}
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			return new String[] { "FALSE" };
		else
			return new String[] { "DEIKTIKA=FALSE" };
	}

}
