-- module Codewars.G964.DblLinear where 
module DblLinear where

-- 0 <= idx <= len
insert :: [Integer] -> Integer -> Int -> [Integer]
insert [] a 0 = [a]
insert (x:xs) a i = if i==0 then a:xs else x:(insert xs a (i-1))
insert [] a i = [a]
-- insert _ _ = []

-- 0 <= i < j < len
swap :: [Integer] -> Int -> Int -> [Integer]
swap (x:xs) 0 j = (xs!!(j-1)) : (insert xs x (j-1))
swap (x:xs) i 0 = (xs!!(i-1)) : (insert xs x (i-1))
swap (x:xs) i j = x:(swap xs (i-1) (j-1))

bubble_up :: [Integer] -> Int -> [Integer]
bubble_up heap i = let p = i `div` 2 in
                       if (heap!!i) < (heap!!p) then bubble_up (swap heap p i) p else heap

bubble_down :: [Integer] -> Int -> [Integer]
bubble_down heap i = let c0 = 2*i+1; c1 = c0+1 in
                       if c0<(length heap) && (heap!!i)>(heap!!c0) then bubble_down (swap heap i c0) c0 else
                       if c1<(length heap) && (heap!!i)>(heap!!c1) then bubble_down (swap heap i c1) c1 else heap

h_insert:: [Integer] -> Integer -> [Integer]
h_insert heap e = bubble_up (heap ++ [e]) (length heap)

-- h_insert :: [Integer] -> [Integer] -> [Integer]
-- h_insert heap elems = foldl h_insert1 heap elems

h_fix :: [Integer] -> [Integer]
h_fix [] = []
h_fix [x] = [x]
h_fix heap = bubble_down ((last heap):(init heap)) 0

generate 0 last _ = last
generate n last l@(min:rest) =  let heap = h_fix rest in
                              if min <= last then generate n last heap else generate (n-1) min (h_insert (h_insert heap ((2*min)+1)) ((3*min)+1))

dblLinear :: Int -> Integer
dblLinear n = generate n 0 [1]


-- generate until n

-- generate :: [Integer] -> [Integer]
-- generate seen to_gen


-- n_to_expand
-- last_expanded
-- to_expand

-- generate 0 last to_expand = last
-- generate n last to_expand = if new <= last then generate n last popped_heap else generate (n-1) new (insert new_heap [(2*n)+1) ,(3*n)+1]) where
--   new:popped_heap = to_expand



-- data MinHeap a = Empty | Node a (MinHeap a) (MinHeap a)
-- len arr = (rangeSize (bounds arr))
-- swapElements i j arr = arr // [(i, arr ! j), (j, arr ! i)]

-- insert1 heap e = bubble_up (heap ++ [e]) (len heap)
-- insert heap elems = foldl insert1 heap elems

-- bubble_up heap 0 = heap
-- bubble_up heap idx = if heap[idx] < heap[p_idx] then bubble_up (swapElements idx p_idx heap) p_idx else heap where p_idx = idx `div` 2
-- bubble_down heap 0 = heap
-- bubble_down heap idx = if c0 >= (len heap) then heap else
--                        if heap[idx] < heap[c0]
--                        then bubble_down (swapElements idx c0 heap) c0
--                        else if heap[idx] < heap[c1]
--                             then bubble_down (swapElements idx c1 heap) c1 
--                             else heap where
--                                       c0 = 2*idx
--                                       c1 = c0+1
                        
--                        (swapElements idx p_idx heap) p_idx else heap where p_idx = idx `div` 2



-- if e <  then Node e ()

-- insert1 (Node a l r) e = if e < a then Node e ()

-- minimum to_expand

-- heap