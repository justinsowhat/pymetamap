pymetamap
=========

Python wrapper around `MetaMap <http://metamap.nlm.nih.gov/>`_.
This will take a list of sentences and extract concepts using MetaMap
then return them in the form of a list of Concept objects.

This is originally written by `Anthony Rios <https://github.com/AnthonyMRios/pymetamap>`_.

I added some minor features and modifications that were necessary while I was working on my thesis using this library.
I thought they might be useful for others too, so I committed my changes here.

How to Install
--------------

>>> python setup.py install

Example Usage
-------------
To use the package, you must have installed a MetaMap instance on your local environment.
For instructions, please go to `MetaMap <https://metamap.nlm.nih.gov/>`_. When using this wrapper,
please start the SKR/Medpost Part-of-Speech Tagger Server in the terminal:
::
    # <public_mm_dir>/bin/skrmedpostctl start

And then start the Word Sense Disambiguation Server:
::
    # <public_mm_dir>/bin/wsdserverctl start

To start you must create a MetaMap instance from the pymetamap package.
::
    >>> from pymetamap import MetaMap
    >>> mm = MetaMap.get_instance('/opt/public_mm/bin/metamap12')

You must supply the metamap binary to ``get_instance()`` in order to
extract concepts.

To extract concepts from a sentence use the ``extract_concepts()``
method. This method taks a list of sentences as input and will return
a list of Concept objects.
::
    >>> sents = ['Heart Attack', 'John had a huge heart attack']
    >>> concepts,error = mm.extract_concepts(sents,[1,2])
    >>> for concept in concepts:
    ...     print concept
    Concept(index='1', mm='MM', score='14.64', preferred_name='Myocardial Infarction', cui='C0027051', semtypes='[dsyn]', trigger='["Heart attack"-tx-1-"Heart Attack"]', location='TX', pos_info='1:12', tree_codes='C14.280.647.500;C14.907.585.500')
    Concept(index='2', mm='MM', score='13.22', preferred_name='Myocardial Infarction', cui='C0027051', semtypes='[dsyn]', trigger='["Heart attack"-tx-1-"heart attack"]', location='TX', pos_info='17:12', tree_codes='C14.280.647.500;C14.907.585.500')

This example shows two seperate concepts extracted via MetaMap from two
different sentences (sentence 1 and sentence 2).


My Minor Modifications
----------------------
As I was using this great python library, I realized that I needed a way to get the
trigger terms as well as the indices of a trigger. So now you can get them by call these
two methods in a Concept class ``get_pos_info()`` and ``get_trigger()``:
::
    >>> for concept in concepts:
    ...     print concept.get_trigger()
    ...     print concept.get_pos_info()
    Heart Attack
    set([(0, 12)])
    heart attack
    set([(16, 28)])


Another modification is to automatically assign an id to each sentence. In the original implementation,
sentences only get an id if you specify it by passing a list of ids, as shown above. Now you can simply pass a list of
sentences as an argument. In this case, the id starts at 0.
::
    >>> concepts,error = mm.extract_concepts(sents)
    >>> for concept in concepts:
    ...     print(concept)
    ConceptMMI(index='0', mm='MMI', score='14.64', preferred_name='Myocardial Infarction', cui='C0027051', semtypes='[dsyn]', trigger='["-- Heart Attack"-tx-1-"Heart Attack"-noun-0]', location='TX', pos_info='1/12', tree_codes='C14.280.647.500;C14.907.585.500')
    ConceptMMI(index='1', mm='MMI', score='13.22', preferred_name='Myocardial Infarction', cui='C0027051', semtypes='[dsyn]', trigger='["-- Heart Attack"-tx-1-"heart attack"-noun-0]', location='TX', pos_info='17/12', tree_codes='C14.280.647.500;C14.907.585.500')
    # the index here is the index of the sentence where the sentence is found



More Information
----------------

Licensed under `Apache 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

Written by Anthony Rios

Modified by Justin So
