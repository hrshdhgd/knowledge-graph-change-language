
# Type: edge deletion


An edge change in which an edge is removed. All edge annotations/properies are removed in the same action.

URI: [ocl:EdgeDeletion](http://w3id.org/oclEdgeDeletion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Node],[Annotation]<annotation%20set%200..1-++[EdgeDeletion&#124;change_description:string%20%3F;about(i):string%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F],[Node]<object%200..1-%20[EdgeDeletion],[Node]<edge%20label%200..1-%20[EdgeDeletion],[Node]<subject%200..1-%20[EdgeDeletion],[EdgeDeletion]uses%20-.->[Deletion],[EdgeChange]^-[EdgeDeletion],[EdgeChange],[Deletion],[Annotation],[Activity])

## Parents

 *  is_a: [EdgeChange](EdgeChange.md) - A change in which the entity changes is an edge

## Uses Mixins

 *  mixin: [Deletion](Deletion.md) - Removal of an element.

## Referenced by class


## Attributes


### Own

 * [annotation set](annotation_set.md)  <sub>OPT</sub>
    * range: [Annotation](Annotation.md)
 * [edge deletion➞change description](edge_deletion_change_description.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [edge label](edge_label.md)  <sub>OPT</sub>
    * range: [Node](Node.md)
 * [object](object.md)  <sub>OPT</sub>
    * range: [Node](Node.md)
 * [subject](subject.md)  <sub>OPT</sub>
    * range: [Node](Node.md)

### Inherited from edge change:

 * [edge change➞about](edge_change_about.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [new value](new_value.md)  <sub>OPT</sub>
    * Description: The value of a property held in the old instance of the ontology
    * range: [String](types/String.md)
 * [old value](old_value.md)  <sub>OPT</sub>
    * Description: The value of a property held in the old instance of the ontology
    * range: [String](types/String.md)
 * [was generated by](was_generated_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | relationship deletion |
