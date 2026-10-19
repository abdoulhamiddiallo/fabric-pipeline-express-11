-- Contrôle dans WH_Chai : lots offerts et vendus par origine, lus dans le lakehouse
SELECT origin, COUNT(*) AS lots, COUNT(price_usd_kg) AS sold FROM LH_Chai.dbo.auction_lots GROUP BY origin ORDER BY lots DESC;
