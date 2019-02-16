(ns foo.core
  (:gen-class))

(defn -main [& args]
  (->> args
       (interpose " ")
       (apply str)
       (println "Executed with the following args: ")))

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))
