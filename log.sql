-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports;
SELECT * FROM crime_scene_reports WHERE day=28 AND month=7 AND street='Chamberlin Street';
SELECT * FROM interviews WHERE day=28 AND month=7;
SELECT * FROM courthouse_security_logs WHERE day=28 AND month=7;
SELECT * FROM courthouse_security_logs WHERE day=28 AND month=7 AND hour=10;


SELECT * FROM atm_transactions WHERE day=28 AND month=7 AND atm_location='Fifer Street';

SELECT * FROM people
JOIN bank_accounts ON people.id=bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number=bank_accounts.account_number
WHERE people.license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55')
AND bank_accounts.account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);


686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X | 49610011 | 686048 | 2010 | 39 | 49610011 | 2020 | 7 | 26 | Fifer Street | withdraw | 10
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X | 49610011 | 686048 | 2010 | 267 | 49610011 | 2020 | 7 | 28 | Fifer Street | withdraw | 50
514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE | 26013199 | 514354 | 2012 | 336 | 26013199 | 2020 | 7 | 28 | Fifer Street | withdraw | 35
396669 | Elizabeth | (829) 555-5269 | 7049073643 | L93JTIZ | 25506511 | 396669 | 2014 | 288 | 25506511 | 2020 | 7 | 28 | Fifer Street | withdraw | 20
467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8 | 28500762 | 467400 | 2014 | 246 | 28500762 | 2020 | 7 | 28 | Fifer Street | withdraw | 48

SELECT * FROM phone_calls WHERE month=7 AND day=28 AND duration<60;
SELECT * FROM phone_calls WHERE month=7 AND day=28 AND duration<60 AND caller IN ('(367) 555-5533', '(367) 555-5533', '(770) 555-1861', '(829) 555-5269', '(389) 555-5198');

phone calls:
233 | (367) 555-5533 | (375) 555-8161 | 2020 | 7 | 28 | 45
255 | (770) 555-1861 | (725) 555-3243 | 2020 | 7 | 28 | 49

SELECT * FROM people 
JOIN passengers ON passengers.passport_number=people.passport_number
JOIN flights ON passengers.flight_id=flights.id
WHERE people.phone_number IN ('(367) 555-5533', '(770) 555-1861')
AND flights. day=29 AND flights.month=7;

514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE | 18 | 3592750733 | 4C | 18 | 8 | 6 | 2020 | 7 | 29 | 16 | 0
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X | 36 | 5773159633 | 4A | 36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20

SELECT * FROM people
JOIN bank_accounts ON people.id=bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number=atm_transactions.account_number
WHERE atm_transactions.day=28 AND atm_transactions.month=7
AND people.phone_number IN ('(367) 555-5533', '(770) 555-1861');

SELECT license_plate FROM people WHERE phone_number IN ('(367) 555-5533', '(770) 555-1861');
SELECT * FROM courthouse_security_logs WHERE day=28 AND month=7 AND hour=10 AND license_plate IN ('322W7JE', '94KL13X');

SELECT * FROM people
JOIN bank_accounts ON people.id=bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number=atm_transactions.account_number
JOIN phone_calls ON phone_calls.caller=people.phone_number
WHERE atm_transactions.day=28 AND atm_transactions.month=7 AND atm_transactions.atm_location='Fifer Street'
AND people.phone_number IN ('(367) 555-5533', '(770) 555-1861')
AND phone_calls.month=7 AND phone_calls.day=28 AND phone_calls.duration<60
AND people.license_plate IN ('94KL13X', '322W7JE');

SELECT * FROM flights WHERE day=29 AND flights.month=7 ORDER BY hour;

SELECT * SELECT airports;

SELECT * from phone_calls
WHERE caller='(367) 555-5533' AND day=28 AND month=7;

SELECT * FROM people 
WHERE phone_number='(375) 555-8161';


