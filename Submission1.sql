-- Question Two: Query Data

-- Question #1
SELECT * FROM Organizations;
SELECT Organization_name, Rating, Location FROM Organizations;
SELECT Club_ID, Membership_cost, Payment_required FROM Details;

-- Question #2
SELECT * FROM Organizations WHERE Rating = 3 AND Number_of_Reviews > 1;
SELECT * FROM Details WHERE Payment_required = "Yes" OR Membership_cost < 500;
SELECT Organization_name, Classification, Rating, Number_of_Reviews FROM Organizations WHERE Rating > 3 AND (Classification = "Special Interest" OR Classification = "Academic");

-- Question #3
SELECT * FROM Organizations WHERE Rating = 2 AND Number_of_reviews > 1 LIMIT 15;
SELECT * FROM Details WHERE Payment_required = "No" OR Membership_cost > 600 LIMIT 5;
SELECT Organization_name, Classification, Rating, number_of_reviews FROM Organizations WHERE Rating > 3 AND (Classification = "Special Interest" OR Classification = "Academic") LIMIT 20;

-- Question #4
SELECT Organization_name, Classification, max(Rating) FROM Organizations;
SELECT Organization_name, Classification, min(Rating) FROM Organizations;
SELECT Club_ID, max(Membership_cost), Payment_required, Description, President FROM Details;

-- Questino #5
SELECT * FROM Organizations
JOIN Details
ON Details.Club_ID = Organizations.Club_ID
WHERE Organizations.Rating = 3
AND Details.Membership_cost > 500 
ORDER BY Membership_cost;

SELECT O.Organization_name, O.Classification, O.Location, D.Payment_required, D.Description FROM Organizations as O
INNER JOIN Details as D
ON O.Club_ID = D.Club_ID
WHERE D.Payment_required = "TRUE"
AND O.Classification = "Fraternity/Sorority";

SELECT O.Organization_name, O.Classification, O.Location, D.Payment_required, D.Description FROM Organizations as O
INNER JOIN Details as D
ON O.Club_ID = D.Club_ID
WHERE D.Payment_required = "FALSE"
AND O.Classification = "Academic";

SELECT * FROM Organizations as O
JOIN Details as D
ON D.Club_ID = O.Club_ID
WHERE Rating > 3
OR (D.Membership_cost > 500
AND Number_of_Reviews = 3)
ORDER BY Rating DESC, Classification;

SELECT O.Club_ID, O.Classification, O.Rating, D.Membership_cost, D.Description, D.President FROM Organizations as O
INNER JOIN Details as D
ON O.Club_ID = D.Club_ID
WHERE O.Rating < 3
OR (D.Membership_cost < 500
AND O.Number_of_Reviews = 2)
ORDER BY D.Membership_cost DESC, O.Rating;

SELECT O.Organization_name, O.Classification, O.Rating, D.Payment_Required, D.Membership_cost, D.Description FROM Organizations as O
INNER JOIN Details as D
ON O.Club_ID = D.Club_ID
WHERE( O.Classification = "Academic"
OR O.Classification = "Special Interest")
AND D.Membership_cost > 700
ORDER BY O.Organization_name;
