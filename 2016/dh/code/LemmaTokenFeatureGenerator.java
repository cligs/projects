package de.uniwue.ds.dsdetection.featuregens;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class LemmaTokenFeatureGenerator extends AKallimachosStandardFeatureGenerator {

	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		String lem = "<unknown>";
		String tok = "<unknown>";
		String pos = "<unknown>";
		for (AnnotationFS afs : covered) {
			if (afs.getFeatureValueAsString(util.getLemmaFeature()) != null)
				lem = afs.getFeatureValueAsString(util.getLemmaFeature());
			if (afs.getFeatureValueAsString(util.getPOSTagFeature()) != null)//NAM
				pos = afs.getFeatureValueAsString(util.getPOSTagFeature());
			tok = afs.getCoveredText();

		}
		if (DSDetectionFeatureGenerators.CSVFORMAT)
			return new String[] { ""+lem, ""+tok, pos };
		else 
			return new String[] {"LEM=" + lem, "TOK=" + tok, "POS=" + pos};
	}

}
