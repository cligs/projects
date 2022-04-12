package de.uniwue.ds.dsdetection.featuregens;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class AmountPPERSentenceFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		int ctrPPER = 0;
		int ctrDET = 0;
		for (AnnotationFS afs : covered) {
			if (afs.getFeatureValueAsString(util.getPOSTagFeature()).equals("PPER")) //PRO:PER
				ctrPPER++;
			if (afs.getFeatureValueAsString(util.getPOSTagFeature()).equals("PPOSAT"))//PRO:POS
				ctrDET++;
		}
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			return new String[] { "" + ctrPPER, "" + ctrDET };
		else
			return new String[] { "APPR=" + ctrPPER, "ADET=" + ctrDET };
	}

}
