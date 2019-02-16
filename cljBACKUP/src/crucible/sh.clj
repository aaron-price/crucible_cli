(ns crucible.sh
  (:require 
    [clojure.java.shell :refer [sh]]
  ))

(defn bash [command]
  (sh "bash" "-c" command))

(defn prnbash [command]
  (println (:out (bash command))))
