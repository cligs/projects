package de.uniwue.ds.dsdetection.featuregens;
import java.util.ArrayList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class FormOfAddressFeatureGenerator extends AKallimachosStandardFeatureGenerator {
	// Todo: Use HashSet
	private static boolean LIST_VALUES = true;
	public final static String[] AUSRUFE = new String[] {"monsieur", "madame", "herr", "frau", "freulein", "herrschaften", "gentlemen", "ladies", "meister", "vater", "mutter", "großmutter", "großvater", "könig", "professor", "königin", "prinzessin", "prinz", "hochwürden", "wachtmeister", "doktor", "verehrte", "verehrter", "graf", "exzellenz", "eminenz", "bischof"};
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
					returnv[i] = "ADDR_" + AUSRUFE[i].toUpperCase() + "=FALSE";
			}
			
		for (AnnotationFS anno : covered) {
			for (int i = 0; i < returnv.length; i++) {
				if (anno.getCoveredText().toLowerCase().equals(AUSRUFE[i]))
					if (DSDetectionFeatureGenerators.CSVFORMAT)
						returnv[i] = "TRUE";
					else {
						if (LIST_VALUES)
							returnv[i] = "ADDR_" + AUSRUFE[i].toUpperCase() + "=FALSE";
						else {
							return new String[] { "ADDR=FALSE" };
						}
						
					}
			}
		}
		if (!LIST_VALUES) {
			return new String[] { "ADDR=FALSE" };
		}
		return returnv;
	}
	
	

}
