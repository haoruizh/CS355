-- CptS 355 - Spring 2020 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW2
     where
import qualified Data.List as List

{- intersect & intersectTail & intersectAll - 22%-}
--intersect
intersect::Eq a => [a] -> [a] -> [a]
--empty inputs
intersect [] [] = []
intersect [] xs = []
intersect xs [] = []
--none empty inputs
intersect (x:xs) ys = List.nub (if elem x ys == True then x:  HW2.intersect xs  ys
                         else HW2.intersect xs ys)

--intersectTail
--helper function
intersectTailHelper::Eq a =>[a] -> [a] -> [a] -> [a]
intersectTailHelper [] [] result= result
intersectTailHelper [] xs result= result
intersectTailHelper xs [] result = result
intersectTailHelper (x:xs) ys result = if elem x ys == True then intersectTailHelper xs ys (result ++ [x]) else (intersectTailHelper xs ys result)
--InsertTail function
intersectTail::Eq a => [a] -> [a] -> [a]
intersectTail xs ys = List.nub(intersectTailHelper xs ys [])

--intersectAll
intersectAll:: Ord a => [[a]] -> [a]
--nonempty case
intersectAll (x:xs)= foldl HW2.intersect x xs

{-2 - partition - 10%-}
partition :: (a->Bool) -> [a] -> ([a], [a])
partition op [] = ([], [])
--nonempty case
partition op xs= (filter op xs, filter (not.op) xs)

{- 3 - sumL, sumMaybe, and sumEither - 27% -}

--sumL
sumHelper::(Num b)=>[b]->b
sumHelper xs = foldr (+) 0 xs
sumL :: (Num b) => [[b]] -> b
sumL xs = sum (map sumHelper xs)


-- sumMaybe 
--add two maybe type num
addMaybe ::(Num a)=> Maybe a->Maybe a->Maybe a
addMaybe Nothing Nothing = Nothing
addMaybe Nothing (Just x1) = (Just x1)
addMaybe (Just x1) Nothing = (Just x1)
addMaybe (Just x1) (Just x2) = (Just (x1+x2))
--Summaybe helper
sumMaybeHelper::(Num b)=>[Maybe b]->Maybe b
sumMaybeHelper xs = (foldr (addMaybe) Nothing  xs)
--sumMaybe
sumMaybe :: (Num a) => [[(Maybe a)]] -> Maybe a
sumMaybe xs =  foldr addMaybe Nothing (map sumMaybeHelper xs)


-- sumEither

data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)
getInt x = read x::Int
--add up function for IEither type
sumIEither :: IEither->IEither->IEither
sumIEither (IInt x) (IInt y) = (IInt (x+y))
sumIEither (IInt x) (IString y) = (IInt (x+(getInt y)))
sumIEither (IString x) (IInt y) = (IInt ((getInt x)+y))
sumIEither (IString x) (IString y) = (IInt ((getInt x)+(getInt y)))
--sumEither helper, add elements in the list together
sumEitherHelper::[IEither]->IEither
sumEitherHelper xs = (foldr (sumIEither) (IInt 0) xs)
--sumEither
sumEither :: [[IEither]] -> IEither
sumEither xs = foldr sumIEither (IInt 0) (map sumEitherHelper xs)

{-4 - depthScan, depthSearch, addTrees - 37%-}

data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)
 
--depthScan
depthScan :: Tree a -> [a]
depthScan (LEAF a) = [a]
depthScan (NODE x x1 x2) = (depthScan x1)++(depthScan x2)++[x] 

--depthSearch
--depthSearch helper function
depthSearchHelper::(Ord p, Num p, Eq a) => Tree a -> a -> p -> p
depthSearchHelper (LEAF x) a currentLevel= if (x==a) then currentLevel else -1
depthSearchHelper (NODE x x1 x2) a currentLevel = if(x==a) then currentLevel
                                                  else if (depthSearchHelper x1 a (currentLevel+1)) /= -1 then depthSearchHelper x1 a (currentLevel+1)
                                                  else if (depthSearchHelper x2 a (currentLevel+1)) /= -1 then depthSearchHelper x2 a (currentLevel+1)
                                                  else -1
depthSearch :: (Ord p, Num p, Eq a) => Tree a -> a -> p
depthSearch (NODE x x1 x2) a = if (depthSearchHelper x1 a 2 > depthSearchHelper x2 a 2) then (depthSearchHelper x1 a 2)
                                   else if (depthSearchHelper x2 a 2 > depthSearchHelper x1 a 2) then (depthSearchHelper x2 a 2)
                                   else if (x==a) then 1
                                   else -1
--addTrees
addTrees :: Num a => Tree a -> Tree a -> Tree a
addTrees (LEAF a) (LEAF b) = (LEAF (a+b))
addTrees (NODE x x1 x2) (NODE y y1 y2) = (NODE (x+y) (addTrees x1 y1) (addTrees x2 y2))
addTrees (NODE x x1 x2) (LEAF y) = (NODE (x+y) x1 x2)
addTrees (LEAF x) (NODE y y1 y2) = (NODE (x+y) y1 y2)
{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}
--Answer to part 5 is in the test file
