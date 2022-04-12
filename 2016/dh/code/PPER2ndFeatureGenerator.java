package de.uniwue.ds.dsdetection.featuregens;
import java.util.ArrayList;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class PPER2ndFeatureGenerator extends AKallimachosStandardFeatureGenerator {

		private static boolean LIST_VALUES = true;
	// Todo: Use HashSet
		public final static String[] MATCHINGPPER = new String[] {"du", "dein", "deiner", "dir", "dich", "ihr", "euer", "euch", "ich", "mein", "meiner", "meines", "mir", "mich", "unser", "uns", "wir"};
		public final static String[] MATCHINGPPER_FR = new String[] {"je", "tu", "nous", "vous", "ma", "mon", "mes", "ta", "ton", "tes", "notre", "nos", "votre", "vos", "toi", "moi", "il", "elle", "ils", "elles", "sa", "son", "ses", "leur"};
		
		public final static String[] MATCHINGPPER_FR_1u2 = new String[] {"je", "tu", "nous", "vous", "ma", "mon", "mes", "ta", "ton", "tes", "notre", "nos", "votre", "vos", "toi", "moi"};
		public final static String[] MATCHINGPPER_FR_3rd = new String[] {"il", "elle", "ils", "elles", "sa", "son", "ses", "leur"};
		@Override
		public String[] generateFeatures(CAS cas, AnnotationFS instance) {
			// instance ist ein Satz
			Util_impl util = new Util_impl(cas);
			List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
			String[] returnv = new String[MATCHINGPPER.length];
			for (int i = 0; i < returnv.length; i++) 
				if (DSDetectionFeatureGenerators.CSVFORMAT)
					returnv[i] = "FALSE";
				else {
						returnv[i] = "PPER_" + MATCHINGPPER[i].toUpperCase() + "=FALSE";
				}
					
				
				
			for (AnnotationFS anno : covered) {
				for (int i = 0; i < returnv.length; i++) {
					if (anno.getCoveredText().toLowerCase().equals(MATCHINGPPER[i]))
						if (DSDetectionFeatureGenerators.CSVFORMAT)
							returnv[i] = "TRUE";
						else {
							if (LIST_VALUES)
								returnv[i] = "PPER_" + MATCHINGPPER[i].toUpperCase() + "=TRUE";
							else {
								return new String[] { "PPER=TRUE" };
								
							}
						}
						
				}
			}
			if (!LIST_VALUES) {
				return new String[] { "PPER=FALSE" };
			}
			return returnv;
		}

	


}
