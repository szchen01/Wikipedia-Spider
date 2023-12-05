package ngordnet.main;

import ngordnet.browser.NgordnetQuery;
import ngordnet.browser.NgordnetQueryHandler;
import ngordnet.ngrams.NGramMap;


import java.util.*;

public class HyponymsHandler extends NgordnetQueryHandler {
    private WordNet wordNet;
    private NGramMap ngm;
    public HyponymsHandler(WordNet wordNet, NGramMap ngm) {
        this.wordNet = wordNet;
        this.ngm = ngm;
    }
    @Override
    public String handle(NgordnetQuery q) {
        List<String> words = q.words();
        int k = q.k();
        Set<String> hyponyms = new TreeSet<>(wordNet.hyponyms(words.get(0)));
        for (int i = 1; i < words.size(); i++) {
            hyponyms.retainAll(wordNet.hyponyms(words.get(i)));
        }
        if (k == 0) {
            return hyponyms.toString();
        } else {
            int startYear = q.startYear();
            int endYear = q.endYear();
            PriorityQueue<Pair> pq = new PriorityQueue<>(k, Comparator.reverseOrder());
            Set<String> returnSet = new TreeSet<>();
            for (String word : hyponyms) {
                List<Double> data = ngm.countHistory(word, startYear, endYear).data();
                Double total = 0.0;
                for (Double n : data) {
                    total += n;
                }
                if (total != 0) {
                    pq.add(new Pair(word, total));
                }
            }
            for (int i = 0; i < k; i++) {
                if (pq.isEmpty()) {
                    break;
                }
                returnSet.add(pq.poll().key);
            }
            return returnSet.toString();
        }
    }

    public class Pair implements Comparable<Pair> {
        private String key;
        private Double value;

        public Pair(String key, Double value) {
            this.key = key;
            this.value = value;
        }

        // getters

        @Override
        public int compareTo(Pair p) {
            return (int) (this.value - p.value);
        }
    }
}
