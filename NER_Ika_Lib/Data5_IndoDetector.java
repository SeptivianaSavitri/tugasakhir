/*****************************************************************

Library of DBpedia Entities Expansion for Indonesian NER

Data5_IndoDetector.java

@Author: Ika Alfina (ika.alfina@gmail.com)
@Last update: 19 Agustus 2016
Fasilkom Universitas Indonesia

Objective: To filter only sentences in Indonesia language using Google Language Detection tool

input: 
  - a file contains sentences --> output of Data4_SentencesFilter.py

output: 
  -  a text file contains all sentences in Indonesian
*********************************************************************/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;

import com.cybozu.labs.langdetect.Detector;
import com.cybozu.labs.langdetect.DetectorFactory;
import com.cybozu.labs.langdetect.LangDetectException;

public class Data5_IndoDetector {
	
	static String input = "newdata/training/prep/ID_formatted1_00.txt";
	static String out = "newdata/training/prep/IDN_formatted1_00.txt";
	
	static String profileDirectory ="language-detection-master/profiles";
	
	public static String isID(String sentence){
		String result = null;
		
		try {
			
			Detector detector = DetectorFactory.create();
			detector.append(sentence);

			result = detector.detect();

		} catch (LangDetectException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return result;
	}
	
	public static void main(String[] args) {	
		BufferedReader br = null;
		PrintStream ps = null;
		try {
			ps = new PrintStream(out);
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		
		try {

			String line;
			String bhs;

			br = new BufferedReader(new FileReader(input));
			
			
			try {
				DetectorFactory.loadProfile(profileDirectory);

				while ((line = br.readLine()) != null) {
					
					bhs = isID(line);
					if(bhs.equals("id")){
						ps.println(line);
					}
				}

			} catch (LangDetectException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		
	}
}
