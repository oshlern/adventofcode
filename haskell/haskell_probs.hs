-- https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca/train/haskell
module SimpleDirections where 

solve :: [String] -> [String]
solve [] = []
solve [x] = 
  let (firstWord:rest) = words x
  in [unwords ("Begin" : rest)]
solve (a:b:rest) = 
  let (a_first:a_rest) = words a
      (b_first:b_rest) = words b
      new_a = case b_first of
                "Left" -> unwords ("Right" : a_rest)
                "Right" -> unwords ("Left" : a_rest)
  in solve (b:rest) ++ [new_a]



-- https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/haskell
module RemoveDups where 

solve :: [Int] -> [Int]
solve [] = []
solve (x:rest) = if seen x rest then solve rest else x:(solve rest)


seen e [] = False
seen e (x:rest) = if e==x then True else seen e rest

-- https://www.codewars.com/kata/514b92a657cdc65150000006/train/haskell
module MultiplesOf3And5 where

solution :: Integer -> Integer
solution number = s (number-1)

s 0 = 0
s n = (if isMultiple n then n else 0)+(s (n-1))

isMultiple n = (mod n 3) == 0 || (mod n 5) == 0

-- https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/haskell
module EvenOrOdd (evenOrOdd) where

evenOrOdd :: (Integral a) => a -> String
evenOrOdd n = if mod n 2 == 0 then "Even" else "Odd"


-- https://www.codewars.com/kata/599d973255342a0ce400009b/train/haskell
{-# LANGUAGE GADTs, DataKinds,
             TypeFamilies, UndecidableInstances #-}

module OddsAndEvens where

-- | The natural numbers.
data Nat = Z | S Nat

-- | The axioms of even numbers.
data Even (a :: Nat) :: * where
  -- | Zero is even.
  ZeroEven :: Even Z
  -- | If n is even, then n+2 is even.
  NextEven :: Even n -> Even (S (S n))

-- | The axioms of odd numbers.
data Odd (a :: Nat) :: * where
  -- | One is odd.
  OneOdd :: Odd (S Z)
  -- | If n is odd, then n+2 is odd.
  NextOdd :: Odd n -> Odd (S (S n))

-- | Proves that if n is even, n+1 is odd.
-- Notice how I use the axioms here.
evenPlusOne :: Even n -> Odd (S n)
evenPlusOne ZeroEven = OneOdd
evenPlusOne (NextEven n) = NextOdd (evenPlusOne n)

-- | Proves that if n is odd, n+1 is even.
oddPlusOne :: Odd n -> Even (S n)
oddPlusOne (OneOdd) = NextEven (ZeroEven)
oddPlusOne (NextOdd n) = NextEven (oddPlusOne n)

-- | Adds two natural numbers together.
-- Notice how the definition pattern matches.
type family   Add (n :: Nat) (m :: Nat) :: Nat
type instance Add Z m = m
type instance Add (S n) m = S (Add n m)

-- | Proves even + even = even
-- Notice how the pattern matching mirrors `Add`s definition.
evenPlusEven :: Even n -> Even m -> Even (Add n m)
evenPlusEven ZeroEven m = m
evenPlusEven (NextEven n) m = NextEven (evenPlusEven n m)

-- | Proves odd + odd = even
oddPlusOdd :: Odd n -> Odd m -> Even (Add n m)
oddPlusOdd OneOdd m = oddPlusOne m
oddPlusOdd (NextOdd n) m = NextEven (oddPlusOdd n m)

-- -- | Proves even + odd = odd
evenPlusOdd :: Even n -> Odd m -> Odd (Add n m)
evenPlusOdd ZeroEven m = m
evenPlusOdd (NextEven n) m = NextOdd (evenPlusOdd n m)

-- | Proves odd + even = odd
oddPlusEven :: Odd n -> Even m -> Odd (Add n m)
oddPlusEven OneOdd m = evenPlusOne m
oddPlusEven (NextOdd n) m = NextOdd (oddPlusEven n m)

-- | Multiplies two natural numbers.
type family   Mult (n :: Nat) (m :: Nat) :: Nat
type instance Mult Z m = Z
type instance Mult (S n) m = Add (Mult n m) m

-- | Proves even * even = even
evenTimesEven :: Even n -> Even m -> Even (Mult n m)
evenTimesEven ZeroEven m = ZeroEven
evenTimesEven (NextEven n) m = evenPlusEven (evenPlusEven (evenTimesEven n m) m) m

-- | Proves odd * odd = odd
oddTimesOdd :: Odd n -> Odd m -> Odd (Mult n m)
oddTimesOdd OneOdd m = m
oddTimesOdd (NextOdd n) m = evenPlusOdd (oddPlusOdd (oddTimesOdd n m) m) m


-- | Proves even * odd = even
evenTimesOdd :: Even n -> Odd m -> Even (Mult n m)
evenTimesOdd ZeroEven m = ZeroEven
evenTimesOdd (NextEven n) m = oddPlusOdd (evenPlusOdd (evenTimesOdd n m) m) m


-- | Proves odd * even = even
oddTimesEven :: Odd n -> Even m -> Even (Mult n m)
oddTimesEven OneOdd m = m
oddTimesEven (NextOdd n) m = evenPlusEven (evenPlusEven (oddTimesEven n m) m) m

-- https://www.codewars.com/kata/59db393bc1596bd2b700007f/train/haskell
{-# LANGUAGE GADTs         #-}
{-# LANGUAGE TypeFamilies  #-}
{-# LANGUAGE TypeOperators #-}

module Kata.AdditionCommutes
  ( plusCommutes ) where

import Kata.AdditionCommutes.Definitions
  ( Z, S
  , Natural(..), Equal(..)
  , (:+:))

-- | if a = b and b = c, then a = c.
transitive :: Equal a b -> Equal b c -> Equal a c
transitive EqlZ EqlZ = EqlZ
transitive (EqlS e_ab) (EqlS e_bc) = EqlS (transitive e_ab e_bc)

-- | S(a+b) = a + S(b)
sDistributes :: Natural a -> Natural b -> Equal (S (a :+: b)) (a :+: (S b))
sDistributes NumZ NumZ = EqlS EqlZ
sDistributes NumZ (NumS b) = EqlS (sDistributes NumZ b)
sDistributes (NumS a) b = EqlS (sDistributes a b)

-- | a + b = b + a
plusCommutes :: Natural a -> Natural b -> Equal (a :+: b) (b :+: a)
plusCommutes NumZ NumZ = EqlZ
-- ____Want to show Z+S(b) = S(b)+Z____
-- Z+S(b) = S(b)   -- implicit from Add
-- S(b)   = S(Z+b) -- implicit from Add
-- S(Z+b) = S(b+Z) -- recurse plusCommutes
-- S(b+Z) = S(b)+Z -- implicit from Add
plusCommutes NumZ (NumS b) = EqlS (plusCommutes NumZ b)
-- ____Want to show (S a)+b = b+(S a)____
-- (S a)+b = S (a+b) -- implicit from Add
-- S (a+b) = S (b+a) -- recurse plusCommutes
-- S (b+a) = b+(S a) -- lemma sDistributes
plusCommutes (NumS a) b = transitive (EqlS (plusCommutes a b)) (sDistributes b a)


-- -- | For any n, n = n.
-- reflexive :: Natural n -> Equal n n
-- reflexive NumZ = EqlZ
-- reflexive (NumS n) = EqlS (reflexive n)

-- -- | if a = b, then b = a.
-- symmetric :: Equal a b -> Equal b a
-- symmetric EqlZ = EqlZ
-- symmetric (EqlS e) = EqlS (symmetric e)

-- For reference, here are the definitions, if you
-- want to copy them into an IDE:
{-

-- For older GHC where Type is not in Prelude
import Data.Kind (Type)

-- | The natural numbers, encoded in types.
data Z
data S n

-- | Predicate describing natural numbers.
-- | This allows us to reason with `Nat`s.
data Natural :: Type -> Type where
    NumZ :: Natural Z
    NumS :: Natural n -> Natural (S n)

-- | Predicate describing equality of natural numbers.
data Equal :: Type -> Type -> Type where
    EqlZ :: Equal Z Z
    EqlS :: Equal n m -> Equal (S n) (S m)

-- | Peano definition of addition.
type family (:+:) (n :: Type) (m :: Type) :: Type
type instance Z :+: m = m
type instance S n :+: m = S (n :+: m)

-}

-- https://www.codewars.com/kata/541c8630095125aba6000c00/train/haskell
module DigitalRoot where

digitalRoot :: Integral a => a -> a
digitalRoot n = if s < 10 then s else digitalRoot s where s = sumDigs n
    
sumDigs 0 = 0
sumDigs n = (n `mod` 10) + sumDigs (n `div` 10)

-- digitalRoot 0 = 0
-- digitalRoot n = if rest == 0 then digit else digitalRoot (digit + (digitalRoot rest)) where 
--     digit = n `mod` 10
--     rest = n `div` 10


-- https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/haskell
module CreatePhoneNumber where

createPhoneNumber :: [Int] -> String
createPhoneNumber ns = 
  let a = take 3 ns
      rest = drop 3 ns
      b = take 3 rest
      c = drop 3 rest
  in "(" ++ (concatMap show a) ++ ") " ++ (concatMap show b) ++ "-" ++ (concatMap show c)


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