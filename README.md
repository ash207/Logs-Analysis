# Logs-Analysis

### About

  The purpose of this project is to use Python and PSQL to work with data that could have come from a real-world web application, with    fields representing information that a web server would record, such as HTTP status codes and URL paths. The Logs_Project.py program is a reporting tool using the `psycopg2` module for answering the following three questions:

    1. What are the most popular three articles of all time? 
    2. Who are the most popular article authors of all time?
    3. On which days did more than 1% of requests lead to errors?

### Requirements

  [Python3] (https://www.python.org/)
  [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)
  [Vagrant] (https://www.vagrantup.com/downloads.html)

### Setup

  1. Download and unzip the [VM configuration] (https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip). This will give you a directory called FSND-Virtual-Machine
  2. `cd` to this directory and then to the vagrant directory located within.
  3. In your terminal bring the virtual machine online by using the command `vagrant up`.
  4. Log into the virtual machine with `vagrant ssh`.
  5. Download this [data] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it, and place the contained SQL file in the vagrant directory.
  6. Load the data with this command: `psql -d news -f newsdata.sql`

### Run

  In your terminal, from the vagrant directory, use the command `python3 Logs_Project.py`. This will create a text file with the answers to the three questions.
