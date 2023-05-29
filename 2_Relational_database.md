1. Intro
    1. each row represent as a entry of the model (Object)
    2. each column represent the attribute of the model (Object)
    3. foreign key are values derived from another table that are used to link the rows between tables and to facilitate searching records. 
        allow us to model specific types of connections between tables.

2. Typical Commands Sample (Postgres)
    - Use pg-admin to maintain db
        - https://www.pgadmin.org/
    1.  Create Table
        - Login to DB Server
        - Go to /Databases/Schemas/Tables/
        - Right click 'query tool'
            - CREATE TABLE people (pk SERIAL PRIMARY KEY,
                name VARCHAR(256) NOT NULL,
                height_cm INT,
                gender VARCHAR(256),
                date_of_birth DATE);
            - CREATE TABLE address (pk SERIAL PRIMARY KEY,
                house_number INT,
                street_name VARCHAR(256),
                city VARCHAR(256),
                country VARCHAR(256));
    2.  Add relationships between 2 tables
        # many people (*) live in 1 address (1)
        # 1 people can have many address (*)
        # many to many relationship
        - Add foreign key to address table, follow the command below
            1. ALTER TABLE address ADD people_pk INT; 
            # add a new field people_pk type INT that map the 'pk' field in 'people' table
            2. ALTER TABLE address ADD FOREIGN KEY (people_pk) REFERENCES people(pk);
            # make 'people_pk' field to foreign key that reference 'pk' field in people table
        - This time add foreign key to people table
            3. ALTER TABLE people ADD address_pk INT; 
            4. ALTER TABLE people ADD FOREIGN KEY (address_pk) REFERENCES address(pk);
        - We can also add foreign key when creating the table in the same time, eg:
             CREATE TABLE cars 
                (pk SERIAL PRIMARY KEY, engine_size_cc INT, 
                colour VARCHAR(256), manufacturer VARCHAR(256), 
                model VARCHAR(256), year INT, people_pk INT, 
                foreign key (people_pk) REFERENCES people(pk))
    3. Insert a data to the table, eg, insert data to people
        - INSERT INTO people 
            (name, height_cm, gender, date_of_birth) 
            VALUES ('Ken', 175, 'Male', '1991-01-01');
        # pk will create automatically, address_pk is null since we yet to add an address.
        - Insert INTO pets, that link up people which it's id is 1:
        INSERT INTO pets (species, coat, age, people_pk) VALUES ('cat', 'brown', 4, 1);
        # for the people_pk, fill with 1 to link to the data which has id=1 in people table

    4. Limitation To Relational Modelling.
        - Graph structure data not easy solve by SQL or relational databasing system
        - it might require many quries to establish the shortest part between 2 nodes in the table,      
        - these kind of structure data can be well fit with graph databasing eg: Neo4j

    5. Database Good Pratices
        - data normalization
            - 1st normal form
                - data is indexed with unique primary key
            - 2nd normal form
                - remove duplicates that depend on aggregates include pk
            - 3rd normal form
                - no transitive dependencies in data
    6. Create tables sample
        # if the table had relation from sub tables, we should create thE sub table first
        1. CREATE TABLE ec(pk SERIAL PRIMARY KEY, EC_name VARCHAR(256));
        2. CREATE TABLE sequencing(pk SERIAL PRIMARY KEY,
            sequencing_factory VARCHAR(256), factory_location VARCHAR(256));
        3. CREATE TABLE genes (pk SERIAL PRIMARY KEY, gene_id VARCHAR(256)
            NOT NULL, entity VARCHAR(256), source VARCHAR(256), start INT,
            stop INT, sequencing_pk INT, ec_pk INT, FOREIGN KEY
            (sequencing_pk) REFERENCES sequencing(pk), FOREIGN KEY (ec_pk)
            REFERENCES ec(pk));
        4. CREATE TABLE products (genes_pk INT, type VARCHAR(256), product
            VARCHAR(256), FOREIGN KEY (genes_pk) REFERENCES genes(pk));
        5. CREATE TABLE attributes (pk SERIAL PRIMARY KEY, key
            VARCHAR(256), value VARCHAR(256));
        6. CREATE TABLE gene_attribute_link(genes_pk INT, attributes_pk
            INT, FOREIGN KEY (genes_pk) REFERENCES genes(pk), FOREIGN KEY
            (attributes_pk) REFERENCES attributes(pk));
    7. Simple inserts
        1. INSERT INTO sequencing (sequencing_factory, factory_location) VALUES
            ('Sanger', 'UK');
        2. INSERT INTO ec (ec_name) VALUES ('oxidioreductase');
        3. INSERT INTO genes (gene_id, entity, source, start, stop, sequencing_pk, ec_pk)
            VALUES ('Gene1', 'Chromosome', 'ena', 190, 255, 1, 1);
            INSERT INTO genes (gene_id, entity, source, start, stop, sequencing_pk, ec_pk)
            VALUES ('Gene2', 'Chromosome', 'ena', 375, 566, CURRVAL('sequencing_pk_seq'),
            CURRVAL('ec_pk_seq'));
        4.  INSERT INTO ec (ec_name) VALUES ('transferase');
        5. INSERT INTO products (genes_pk, type, product) VALUES
            (1, 'gene', 'mrna'), (1, 'cds', 'protein'),
            (2, 'gene', 'mrna'), (2, 'cds', 'protein');
        6. INSERT INTO attributes (key, value) VALUES
            ('ID', 'gene:b001'),
            ('Name', 'thrL'),
            ('biotype', 'protein_coding'),
            ('description', 'thr operon leader peptide'),
            ('Name', 'fucA'),
            ('description', 'Fructokinase A');
        7. INSERT INTO gene_attribute_link (genes_pk, attributes_pk) VALUES
            (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 3), (2, 5), (2, 6);
    7. Simple queries
        - select * from genes, ec;
            # there're many gene to 1 ec; so if there're 5 genes, but 2 ec that mapped,
            # it will return 5*2 = 10 rows, but it doesn't make sense since 1 gene will only have 1 ec name
        - select * from genes, ec where genes.ec_pk = ec.pk;
            # add condition so the return combine data will be restricted.
        - select gene_id, entity, ec_name, sequencing_factory, factory_location 
            FROM genes, ec, sequencing 
            WHERE genes.ec_pk = ec.pk AND genes.sequencing_pk = sequencing.pk;
            # example join 3 tables together by pk
        -  SELECT gene_id, key, value 
            FROM genes, attributes, gene_attribute_link
            WHERE genes.pk = gene_attribute_link.genes_pk AND attributes.pk = gene_attribute_link.attributes_pk;
        - INNER JOIN example, for example
            # -- select * from genes, ec where genes.ec_pk = ec.pk;
            # -- or using inner join
            - select * from genes INNER JOIN ec ON genes.ec_pk = ec.pk;
    8. database query optimization
        # create INDEX for frequently use columns
        - CREATE INDEX entity_index ON genes (entity);
        # when search by 'entity' in genes table, it will become more faster
        - select * from genes where entity = '...';
        # we can use EXPLAIN to check the procedure during query
        - EXPLAIN SELECT * from genes, ec where genes.ec_pk = ec.pk;
        # We can further add ANALYZE to produce the estimated time for evaluate the query
        - EXPLAIN ANALYZE SELECT * from genes, ec where genes.ec_pk = ec.pk;
        # Use nested SUB query to reduce the total combination of the rows first to do further join query
        1. Not using nested query
            - SELECT * FROM genes, ec WHERE genes.ec_pk = ec.pk;
        2. Using nested query
            - SELECT nested_table.*, ec.* FROM (SELECT * FROM genes WHERE entity = 'Chromosome') nested_table INNER JOIN ec ON nested_table.ec_pk = ec.pk;
        # 2 approachs :
            1. # denormalizing 2 tables, 
                # actually just join 2 tables together if user's frequetly join those tables during query.
                # in short, add all column from ec table to genes;
                # I think it quite discourage unless we sure those tables can be completely redundant to combine it as a single table.
                - CREATE TABLE genes_with_ec (
                    pk SERIAL PRIMARY KEY, gene_id VARCHAR(256) NOT NULL, 
                    entity VARCHAR(256), source VARCHAR(256), start INT, stop INT,
                    sequencing_pk INT, ec_name VARCHAR(256), 
                    FOREIGN KEY (sequencing_pk) REFERENCES sequencing(pk));
            2. Materialized View
                # form of adjuncts table that contains the contents of the query.
                - CREATE MATERIALIZED VIEW gene_ec_view AS 
                    SELECT gene_id, entity, source, start, stop, sequencing_pk, ec_name 
                    FROM genes, ec 
                    WHERE genes.ec_pk = ec.pk;
                # then we could query the data as a normal table
                # the cost is way more faster then join 2 tables,
                    EXPLAIN ANALYZE SELECT gene_id, entity, source, start, stop, sequencing_pk, ec_name 
                    FROM genes, ec 
                    WHERE genes.ec_pk = ec.pk;
                    EXPLAIN ANALYZe SELECT * FROM gene_ec_view;
                # *** Noticed that in Postgres materialized view will not refresh on the underlying tables genes, ec is updated.
                # We need to run the following command to refresh the materialized table
                    - REFRESH MATERIALIZED VIEW gene_ec_view;
                
        9.  SQC fuctions
                select count(*) FROM genes;
                SELECT MIN(start) FROM GENES;
                SELECT MAX(start) FROM GENES;
                SELECT SUM(start) FROM GENES;
                SELECT AVG(start) FROM GENES;
                SELECT ROUND(AVG(start)) FROM GENES;
                SELECT entity, LOWER(entity), UPPER(entity), LENGTH(entity) FROM GENES;
                SELECT NOW();
                SELECT entity, MAX(start) FROM GENES GROUP BY entity;
        10. Altering database
            -- delete database
            drop database ooops;
            -- delete table;
            drop table sometableName;
            -- Remove column 'source'
            ALTER TABLE genes DROP COLUMN source CASCADE;
            -- Noticed that the materialized View 'gene_ec_view' will be removed once it update
            SELECT * FROM GENES;
            -- Added column 
            ALTER TABLE genes ADD COLUMN sense CHAR(255);
            ALTER Table GENES ADD COLUMN start_codon CHAR(255) DEFAULT('M');
            -- Update Column
            UPDATE genes SET sense = '+' WHERE gene_id='Gene1';
            Update genes SET sense ='-' WHERE pk=2 or pk=3;
            UPDATE genes SET sense = 'U' WHERE entity = 'Plasmid';
            UPDATE genes SET start = 558, stop=569 WHERE pk=4;
            SELECT * FROM GENES;

        12. create data model with Django
            - 
