-- https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/haskell
module Codewars.Kata.Permutations (permutations) where

permutations :: String -> [String]
permutations "" = [""]
permutations (a:as) = removeDups (concat (map (ins a) (permutations as)))

removeDups :: [String] -> [String]
removeDups [] = []
removeDups (a:as) = if elem a as then removeDups as else a:(removeDups as)

ins :: Char -> String -> [String]
ins c "" = [[c]]
ins c s@(a:as) = (c:s):(ins c as)