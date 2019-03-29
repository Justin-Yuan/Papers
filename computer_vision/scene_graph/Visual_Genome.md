# Visual Genome 
[link](https://visualgenome.org/static/paper/Visual_Genome.pdf)

## Intro 

- 3 key elements 
    - a grounding of visual concepts to language 
    - more complete set of descriptions and QAs for each image based on multiple image regions 
    - a formalized representation of the components of an image 
- knowledge base representation in NLP to represent object relations -> scene graph 
- all objects, attributes and relationships are canonicalized to its corresponding WordNet ID (synset ID)

## Modeling 

- main components: region descriptions, objects, attributes, relationships, region graphs, scene graphs, question answer pairs
- free-form QA (based on the entire image) & region-based QA, 6 types of question per image: what, where, how, when, who, why 