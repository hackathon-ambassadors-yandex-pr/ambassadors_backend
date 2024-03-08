#!/bin/sh

while ! nc -z ambassadors_postgres 5432;
    do sleep .5;
    echo "wait database";
done;
    echo "connected to the database";
