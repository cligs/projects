package de.uniwue.ds.dsdetection.featuregens;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class VerbFormFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {

		String[] verbforms = new String[] { "VER:cond", "VER:impe", "VER:pres", "VER:simp", "VER:futu", "VER:impf",
				"VER:infi", "VER:pper", "VER:ppre", "VER:subi", "VER:subp" };
		String[] labels = new String[] { "VER:cond", "VER:impe", "VER:pres", "VER:simp", "VER:futu", "VER:impf",
				"VER:infi", "VER:pper", "VER:ppre", "VER:subi", "VER:subp" };
		
		verbforms = new String[] { "VVFIN", "VAFIN", "VMFIN" , "VVIMP", "VAIMP" , "VVINF", "VVIZU", "VAINF", "VMINF" , "VVPP", "VMPP", "VAPP"};
		labels = new String[] { "VVFIN", "VAFIN", "VMFIN" , "VVIMP", "VAIMP" , "VVINF", "VVIZU", "VAINF", "VMINF" , "VVPP", "VMPP", "VAPP"};

		if (DSDetectionFeatureGenerators.CSVFORMAT)
			verbforms = new String[] { "", "", "", "", "", "", "", "", "", "", "" };

		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		HashMap<String, Integer> count = new HashMap<String, Integer>();
		for (String s : labels) {
			count.put(s, 0);
		}

		for (AnnotationFS afs : covered) {
			for (String s : labels) {
//				System.out.println(afs.getFeatureValueAsString(util.getPOSTagFeature()));
				if (afs.getFeatureValueAsString(util.getPOSTagFeature()).equals(s))
					count.put(s, 1);// count.get(s) + 1);
			}
		}

		for (int i = 0; i < labels.length; i++) {
			int c = count.get(labels[i]);
			if (DSDetectionFeatureGenerators.CSVFORMAT)
				verbforms[i] += "" + c;
			else
				verbforms[i] += "=" + c;
		}
		return verbforms;
	}

}
