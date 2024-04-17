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

