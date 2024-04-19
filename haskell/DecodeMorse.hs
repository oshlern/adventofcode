
-- https://www.codewars.com/kata/54b724efac3d5402db00065e/train/haskell
module Codewars.Kata.DecodeMorse (decodeMorse) where

import Codewars.Kata.DecodeMorse.Preload (morseCodes)

import Data.Map.Strict ((!))
import Data.List.Split (splitOn)

decodeMorse :: String -> String
decodeMorse s = unwords (map (concat . (map (morseCodes !)) . (splitOn " ")) (splitOn "   " (noSpace s)))

noSpace "" = ""
noSpace (a:as) = if a == ' ' then (noSpace as) else noEndSpace (a:as)
noEndSpace "" = ""
noEndSpace s = if (last s) == ' ' then noEndSpace (init s) else s

-- https://www.codewars.com/kata/54b72c16cd7f5154e9000457/solutions/haskell
module Kata.DecodeMorseAdvanced where

import Kata.DecodeMorseAdvanced.Preload    -- holds the "morseCodes" data structure for you
import Data.List
import Data.List.Split (splitOn)

decodeBits :: String -> String
decodeBits bits = pChar bs
  where
    process = map length
            . group
            . dropWhileEnd ('0'==)
            . dropWhile ('0'==) 
    bs = process bits
    l = minimum bs
    pChar [] = ""
    pChar (a:as) = (if a == l then "." else "-") ++ (pSpace as)
    pSpace [] = ""
    pSpace (a:as) = (if a == l then "" else if a == 3*l then " " else "   ") ++ (pChar as)

decodeMorse :: String -> String
decodeMorse = unwords
            . map (concat . (map (morseCodes !)) . (splitOn " "))
            . splitOn "   "



module Haskell.Codewars.MorseDecoder where 
import Haskell.Codewars.MorseDecoder.Preloaded (morseCode)
import Data.Maybe
import Data.List
import Data.List.Split (splitOn)

-- estimateL s = 3
-- 7 0s is a great sign!
-- just use 1's, find cutoff which makes least errors? distance?
estimateL :: [Double] -> Double
-- estimateL bs = minimum bs

-- estimateL bs = if 1.7*min > max then sqrt (min*max) else sqrt (min*max/3)
estimateL ls = mean
  where
--     ones = filter (\x -> (x /= "" && (head x) == 1)) bs
--     ls = map (0.5 +) ls
--     min = minimum ls
--     ls_norm = map (\x -> x/min) ls
--     sevens = filter (4.6 <) ls_norm
--     ls_not7 = filter (4.6 >=) ls_norm
--     threes = filter (1.75 >) ls_not7
--     ones = filter (1.75 <=) ls_not7
--     one7 = if sevens == [] then 1 else (sum sevens / fromIntegral (length sevens)) / 7
--     one3 = if threes == [] then 1 else (sum threes / fromIntegral (length threes)) / 3
--     one1 = if ones == [] then 1 else sum ones / fromIntegral (length ones)
--     one1 = (sum (filter (1 <=) ls))
--     one1 = (sum ls)
    one1 = sum ls / fromIntegral (length ls)
    one3 = one1
    one7 = one1
--     prod = one1*one3*one7
    ones = [3]
    twos = 
    n = length (filter (\x -> if x = [] \= then 0 else 1) [ones, threes, sevens])
    mean = (one1*one3*one7) ** (1 / fromIntegral 3)
--     mean = one1 ** (1 / fromIntegral 3)

--     ones = everyother bs
--     min = 0.5 + minimum ones
--     max = 0.5 + maximum ones

everyother [] = []
everyother [x] = [x]
everyother (x:y:xs) = x : everyother xs




-- argmax_l P min(e^-(n-l)^2, e^-(n-3l)^2)
-- argmax_l S min((n-l)^2, (n-3l^2))
-- argmax_l S n^2-2nl+l^2 + min(2l^2 - 4nl, 0)
-- argmax_l S -2nl+l^2 + min(2l^2 - 4nl, 0)
-- argmax_l -2mnl+nl^2 + S min(2l^2 - 4il, 0)
-- argmax_l nl(l-2m) + 2*S min(l(l-2*i), 0)
-- argmax_l nl(l-2m) + nl(9l-6m)
-- argmax_l nl(10l-8m)
-- argmin_l nl(10l-8m) 
-- (10l-8m)+10l = 20l-8m ==> l = 2/5 m 
-- argmax_l S l*(l-2n) + min(2l^2 - 4nl, 0)
decodeBitsAdvanced :: String -> String
-- decodeBitsAdvanced s = s
-- decodeBitsAdvanced bits = if bs == [] then "" else (pChar bs) -- ++ (show l)
decodeBitsAdvanced bits = if bs == [] then "" else (show l)
  where
    process = map (fromIntegral . length)
            . group
            . dropWhileEnd ('0'==)
            . dropWhile ('0'==) 
    bs = process bits
    l = estimateL bs
    pChar :: [Double] -> String
    pChar [] = ""
    pChar (a:as) = (if a < 1.75*l then "." else "-") ++ (pSpace as)
    pSpace :: [Double] -> String
    pSpace [] = ""
    pSpace (a:as) = (if a < 1.75*l then "" else if a < 4.6*l then " " else "   ") ++ (pChar as)

-- decodeBits :: String -> String
-- decodeBits bits = pChar bs
--   where
--     process = map length
--             . group
--             . dropWhileEnd ('0'==)
--             . dropWhile ('0'==) 
--     bs = process bits
--     l = estimateL bs
--     pChar [] = ""
--     pChar (a:as) = (if a == l then "." else "-") ++ (pSpace as)
--     pSpace [] = ""
--     pSpace (a:as) = (if a == l then "" else if a == 3*l then " " else "   ") ++ (pChar as)

decodeMorse :: String -> String
decodeMorse s = s
-- decodeMorse = unwords
--             . map (concat . (map (get morseCode)) . (splitOn " "))
--             . splitOn "   "

get :: [(String, String)] -> String -> String
get [] s = "[" ++ s ++"]"
-- get [] s = ""
get ((key, val):rest) s = if key == s then val else get rest s


