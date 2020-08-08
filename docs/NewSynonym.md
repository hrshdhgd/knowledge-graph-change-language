
# Type: new synonym


A node change where a de-novo synonym is created

URI: [ocl:NewSynonym](http://w3id.org/oclNewSynonym)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NodeSynonymChange],[NodeSynonymChange]^-[NewSynonym&#124;about(i):string%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F],[Activity])

## Parents

 *  is_a: [NodeSynonymChange](NodeSynonymChange.md)

## Attributes


### Own

 * [new value](new_value.md)  <sub>OPT</sub>
    * Description: The value of a property held in the old instance of the ontology
    * range: [String](types/String.md)

### Inherited from node synonym change:

 * [node change➞about](node_change_about.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [old value](old_value.md)  <sub>OPT</sub>
    * Description: The value of a property held in the old instance of the ontology
    * range: [String](types/String.md)
 * [was generated by](was_generated_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)