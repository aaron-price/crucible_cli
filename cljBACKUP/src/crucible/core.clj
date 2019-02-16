(ns crucible.core
  (:require 
    [clojure.java.shell :refer [sh]]
    [crucible.sh :refer [bash prnbash]])
  (:gen-class))


(defn -main [& args]
  (sh "cl")
  (->> args
       (interpose " ")
       (apply str)
       (println "Executed with the following args: ")))
