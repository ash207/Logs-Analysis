#!/usr/bin/python

import psycopg2

# 1. Query for the three most popular articles
popular_articles = """
    SELECT
        title,
        COUNT(path) AS Views
    FROM
        log,
        articles
    WHERE path LIKE '/article/%'
      AND slug = SUBSTRING(path, 10)
    GROUP BY title
    ORDER BY Views DESC
    LIMIT 3;"""

# 2. Query for the most popular authors
popular_authors = """
    SELECT
        name,
        COUNT(path) AS Views
    FROM
        log,
        articles,
        authors
    WHERE path LIKE '/article/%'
      AND slug = SUBSTRING(path, 10)
      AND authors.id = articles.author
    GROUP BY name
    ORDER BY Views DESC;"""

# 3. Query for days when more than 1% of requests resulted in errors
errors = """
    SELECT *
    FROM
        (SELECT
            to_char(time, 'FMMonth DD, YYYY'),
            round(100.0*sum(CASE WHEN log.status = '404 NOT FOUND'
            THEN 1 END)/count(log.status),1) AS Percent_Error
        FROM log
        GROUP BY to_char(time, 'FMMonth DD, YYYY')) AS alias
    WHERE Percent_Error > 1;"""


def get_reports(psql_query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(psql_query)
    report = c.fetchall()
    db.close()
    return report

Report_1 = dict()
Report_2 = dict()
Report_3 = dict()

Report_1['report'] = get_reports(popular_articles)
Report_2['report'] = get_reports(popular_authors)
Report_3['report'] = get_reports(errors)

with open("Report.txt", "w") as text_file:
    print("FSND: Logs Analysis Project" + '\n\n', file=text_file)
    print("Top Articles:" + '\n', file=text_file)
    for report in Report_1['report']:
        print('\t' + '"' + str(report[0]) + '"' + ' - ' +
              str(report[1]) + ' Total Views', file=text_file)
    print('\n\n' + "Top Authors:" + '\n', file=text_file)
    for report in Report_2['report']:
        print('\t' + str(report[0]) + ' - ' +
              str(report[1]) + ' Total Views', file=text_file)
    print('\n\n' + "Days with more than 1% of request errors:" +
          '\n', file=text_file)
    for report in Report_3['report']:
        print('\t' + report[0] + ' - ' +
              str(report[1]) + '% errors', file=text_file)
