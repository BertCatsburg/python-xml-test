# XML Testing in Python with SAX

How to process a big XML file with Python SAX.

The goal of this small project is to process a XML file and split it up in Chunks.

A Chunk is defined as a piece of XML which is a part of the big XML.

For example:

```xml

<collection shelf="New Arrivals">
    <movie title="Enemy Behind" subTitle="There is an Enemy Behind">
        <type>War, Thriller</type>
        <format>DVD</format>
        <date>
            <year>2003</year>
            <month>August</month>
            <day>12</day>
        </date>
        <rating>PG</rating>
        <stars>10</stars>
        <description>Talk about a US-Japan war</description>
    </movie>
    <radioshow title="Dirty Talk Radio">
        <type>Comedy</type>
        <format>MP3</format>
        <rating>R</rating>
        <stars>5</stars>
    </radioshow>
    <movie title="Ishtar">
        <type>Comedy</type>
        <format>VHS</format>
        <rating>PG</rating>
        <stars>2</stars>
        <description>Viewable boredom</description>
    </movie>
</collection>
```

The big XML is 'collection', 
but we want chunks of 'movie' or 'radioshow'.

This is what the project does, 
but what is does more is show how you can process a 
big XML file. 
