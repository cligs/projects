package de.uniwue.ds.dsdetection.featuregens;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

import org.apache.uima.cas.CAS;
import org.apache.uima.cas.text.AnnotationFS;

import de.uniwue.ds.dsdetection.main.DSDetectionFeatureGenerators;
import de.uniwue.mk.kall.mlf.featureRepresentation.formats.AKallimachosStandardFeatureGenerator;
import de.uniwue.mkrug.kall.typesystemutil.Util_impl;

public class VerbCatFeatureGenerator extends AKallimachosStandardFeatureGenerator {
	public final String verbcatfile = "verbcats.txt";

	public Hashtable<String, String> verbs = new Hashtable<String, String>();

	public HashSet<String> cats = new HashSet<String>();

	public VerbCatFeatureGenerator() {
		super();
		Scanner s;
		try {
			s = new Scanner(new File(verbcatfile));
			while (s.hasNextLine()) {
				String line = s.nextLine();
				verbs.put(line.split("\t")[0].toLowerCase(), line.split("\t")[1].toLowerCase());
				cats.add(line.split("\t")[1].toLowerCase());
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	// VERB.WEATHER=1 VERB.CONTACT=0 VERB.MOTION=0 VERB.BODY=0
	// VERB.COMPETITION=0 VERB.POSSESSION=0 VERB.SOCIAL=0 VERB.EMOTION=0
	// VERB.COGNITION=0 VERB.STATIVE=4 VERB.CREATION=0 VERB.PERCEPTION=0
	// VERB.CHANGE=0 VERB.CONSUMPTION=0 VERB.COMMUNICATION=1

	// VERB.STATIVE=4!!
	@Override
	public String[] generateFeatures(CAS cas, AnnotationFS instance) {
		// instance ist ein Satz
		Util_impl util = new Util_impl(cas);
		List<AnnotationFS> covered = util.getCovered(instance, util.getPOSType());
		LinkedList<String> list = new LinkedList<String>();
		String cat = null;
		// cats.clear();
		// cats.add("verb.COMMUNICATION".toLowerCase());
		for (String c : cats) {
			int catcount = 0;
			for (AnnotationFS afs : covered) {
				if (afs.getFeatureValueAsString(util.getLemmaFeature()) == null || afs.getFeatureValueAsString(util.getLemmaFeature()) == null )
					continue;
				if ((cat = verbs.get(afs.getFeatureValueAsString(util.getLemmaFeature()).toLowerCase())) != null
						&& cat.equals(c)) {
					catcount++;
					// break;
				}
			}
			if (DSDetectionFeatureGenerators.CSVFORMAT)
				list.add("" + ((catcount) > 0));
			else
				list.add(c.replace(".", "_").toUpperCase() + "=" + ((catcount) > 0));
		}
		return list.toArray(new String[list.size()]);
	}

}
