-- CptS 355 - Spring 2020 Assignment 1
-- Author: Haorui Zhang
--Discussed with: 

module HW1
     where

-- 1a. exists
exists :: Eq t=>t->[t]->Bool
--empty list, return false
exists n [] = False
--If n is in the list return True
exists n (x:xs) |n==x=True
                |otherwise = exists n xs

-- 1b. type for exists


-- 1.c countInList
countInList :: (Num p, Eq t)=>t->[t]->p
--empty list return 0
countInList t []=0
--count t in list xs
countInList t (x:xs) |t==x=(1+countInList t xs)
                    |otherwise = countInList t xs


-- 2. listDiff
--remove the element in ys list that is same as x, return the list
removeSameElement :: Eq t=>t->[t]->[t]
--empty list, return empty list
removeSameElement x [] = []
--remove the same element
removeSameElement n (x:xs) |x==n = xs
                         |otherwise = x : removeSameElement n xs

--listDiff
listDiff :: Eq a=>[a]->[a]->[a]
--empty list case
listDiff x [] = x
listDiff [] y = []
--noneEmpty case. Return the difference between two lists
listDiff(x:xs) (y:ys) |(countInList y (x:xs) /=0) = listDiff (removeSameElement y (x:xs)) ys
                         |otherwise = listDiff (x:xs) ys

-- 3. firstN
firstN :: (Ord t, Num t) => [a]->t->[a]
--empty => return empty
firstN [] t = []
--return 1st~t th item in the list xs
firstN (x:xs) t |t>0=x:firstN xs (t-1)
               |otherwise=[]


-- 4. busFinder
busFinder::Eq t=> t -> [(a,[t])]->[a]
--if bus list is empty
busFinder t [] = []
--return a list contains the bus that has stop t
busFinder t (x:xs) | (exists t (snd(x))) = fst(x):busFinder t xs
                    |otherwise = busFinder t xs

-- 5. cumulativeSums
--Helper. Return a list with cumulative sum
sumHelper :: Num a=>a->[a]->[a]
--empty list, return list with n
sumHelper n [] = [n]
--cumulative the sum and append it the list
sumHelper n (x:xs) = n : (sumHelper (n+x) xs)

--cumulativeSums
cumulativeSums :: Num a =>[a]->[a]
--empty list return empty list
cumulativeSums [] = []
--call helper and return the list of sums
cumulativeSums (x:xs) = let y = sumHelper x xs
                         in y



-- 6. groupNleft
groupNleft :: Int->[a]->[[a]]
--empty list
groupNleft t [] = []
--Using SplitAt function to get the first and second parts
groupNleft t xs = (fst(splitAt t xs)): groupNleft t (snd(splitAt t xs))


