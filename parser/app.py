from flask import (
    Flask,
    render_template,
    request,
)
from kgcl import (
    NodeRename,
    NodeObsoletion,
    NodeUnobsoletion,
    NodeDeletion,
    NodeMove,
    NodeDeepening,
    NodeShallowing,
    EdgeCreation,
    EdgeDeletion,
    PredicateChange,
    NodeCreation,
    ClassCreation,
    NewSynonym,
    RemovedNodeFromSubset,
)
import parser
import graph_transformer
import rdflib

app = Flask(__name__)


# we could store changes in a data base - do we want to
@app.route("/", methods=["POST", "GET"])
def index():
    # TODO: get examples from folder structure
    examples = [
        "rename",
        "nodeCreation",
        "nodeDeletionByLabel",
        "nodeDeletionById",
        "obsoleteByLabel",
        "obsoleteById",
        "unobsoleteById",
        "nodeDeepening",
        "nodeShallowing",
        "move",
        "edgeCreation",
        "edgeDeletion",
    ]

    if request.method == "POST":

        if "apply_changes" in request.form:

            # get input graph from form
            graphInput = request.form["graph"]

            # get input kgcl statements from form
            kgcl = request.form["kgcl"]

            # TODO:
            # 1. load triples without writing to a file first
            # 2. handle kgcl input without writing to a file

            # store kgcl statements
            f = open("testData/kgcl", "w")
            f.write(kgcl)
            f.close()

            # parse KGCL input
            parsed_statements = parse(kgcl)

            # store graph as file
            f = open("testData/graph.nt", "w")
            f.write(graphInput)
            f.close()

            # load input graph from file
            g = rdflib.Graph()
            g.load("testData/graph.nt", format="nt")

            # transform graph
            graph_transformer.transform_graph(parsed_statements, g)

            # save graph
            # TODO: get text representation of graph without writing to a file
            g.serialize(destination="testData/transformation.nt", format="nt")

        if "load_example" in request.form:
            select = request.form.get("comp_select")
            example = str(select)

            f = open("testData/example/" + example + "/graph.nt", "r")
            graph = f.read()
            f.close()

            f = open("testData/graph.nt", "w")
            f.write(graph)
            f.close()

            f = open("testData/example/" + example + "/kgcl", "r")
            kgcl = f.read()
            f.close()

            f = open("testData/kgcl", "w")
            f.write(kgcl)
            f.close()

            # parse KGCL input
            parsed_statements = parse(kgcl)

            # load input graph from file
            g = rdflib.Graph()
            g.load("testData/graph.nt", format="nt")

            # transform graph
            graph_transformer.transform_graph(parsed_statements, g)

            # save graph
            g.serialize(destination="testData/transformation.nt", format="nt")

        # load graph
        f = open("testData/graph.nt", "r")
        graph = f.read()
        f.close()

        # load kgcl
        f = open("testData/kgcl", "r")
        kgcl = f.read()
        f.close()

        # parse KGCL input
        output = parse(kgcl)

        # prepare parsed
        output_rendering = ""
        for o in output:
            output_rendering += render(o) + "\n"

        # load transformed graph
        f = open("testData/transformation.nt", "r")
        transformation = f.read()
        f.close()

        return render_template(
            "index.html",
            inputGraph=graph,
            inputKGCL=kgcl,
            parsedKGCL=output_rendering,
            outputGraph=transformation,
            examples=examples,
        )

    else:
        return render_template("index.html", examples=examples)


def parse(input):
    return parser.parse(input)


def render(kgclInstance):
    render = ""
    if type(kgclInstance) is NodeRename:
        render = (
            render
            + "NodeRename("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Old Value="
            + kgclInstance.old_value
            + ", "
            + "New Value="
            + kgclInstance.new_value
            + ")"
        )

    if type(kgclInstance) is NodeObsoletion:
        render = (
            render
            + "NodeObsoletion("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Repacelement="
            + str(kgclInstance.has_direct_replacement)
            + ", "
            + "About="
            + kgclInstance.about_node
            + ")"
        )

    if type(kgclInstance) is NodeDeletion:
        render = (
            render
            + "NodeDeletion("
            + "ID="
            + kgclInstance.id
            + ", "
            + "About="
            + kgclInstance.about_node
            + ")"
        )

    if type(kgclInstance) is ClassCreation:
        render = (
            render
            + "ClassCreation("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Term_ID"
            + kgclInstance.node_id
            + ")"
        )

    if type(kgclInstance) is NodeCreation:
        render = (
            render
            + "NodeCreation("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Term ID="
            + kgclInstance.node_id
            + ", "
            + "Label="
            + kgclInstance.name
            + ")"
        )

    if type(kgclInstance) is NodeMove:
        render = (
            render
            + "NodeMove("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Old Value="
            + kgclInstance.old_value
            + ", "
            + "New Value="
            + kgclInstance.new_value
            + ")"
        )

    if type(kgclInstance) is NodeUnobsoletion:
        render = (
            render
            + "NodeUnobsoletion("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Term id="
            + kgclInstance.about_node
            + ")"
        )

    if type(kgclInstance) is NodeDeepening:
        render = (
            render
            + "NodeDeepening("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Term ID="
            + kgclInstance.about_edge.subject
            + ", "
            + "Old Value="
            + kgclInstance.old_value
            + ", "
            + "New Value="
            + kgclInstance.new_value
            + ")"
        )

    if type(kgclInstance) is NodeShallowing:
        render = (
            render
            + "NodeShallowing("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Term ID="
            + kgclInstance.about_edge.subject
            + ", "
            + "Old Value="
            + kgclInstance.old_value
            + ", "
            + "New Value="
            + kgclInstance.new_value
            + ")"
        )

    if type(kgclInstance) is EdgeCreation:
        render = (
            render
            + "EdgeCreation("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Subject="
            + kgclInstance.subject
            + ", "
            + "Predicate="
            + kgclInstance.predicate
            + ", "
            + "Object="
            + kgclInstance.object
            + ")"
        )

    if type(kgclInstance) is EdgeDeletion:
        render = (
            render
            + "EdgeDeletion("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Subject="
            + kgclInstance.subject
            + ", "
            + "Predicate="
            + kgclInstance.predicate
            + ", "
            + "Object="
            + kgclInstance.object
            + ")"
        )

    if type(kgclInstance) is NewSynonym:
        render = (
            render
            + "NewSynonym("
            + "ID="
            + kgclInstance.id
            + ", "
            + "About Node="
            + kgclInstance.about_node
            + ", "
            + "Synonym="
            + kgclInstance.new_value
            + ")"
        )

    if type(kgclInstance) is PredicateChange:
        render = (
            render
            + "PredicateChange("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Subject="
            + kgclInstance.about_edge.subject
            + ", "
            + "Subject="
            + kgclInstance.about_edge.object
            + ", "
            + "Old Value="
            + kgclInstance.old_value
            + ", "
            + "New Value"
            + kgclInstance.new_value
            + ")"
        )

    # if(type(kgclInstance) is AddNodeToSubset):
    #    render = render + "AddNodeToSubset(" \
    #            + "ID=" + kgclInstance.id + ", " \
    #            + "Subset=" + kgclInstance.in_subset + ", " \
    #            + "About Node" + kgclInstance.about_node + ")"

    if type(kgclInstance) is RemovedNodeFromSubset:
        render = (
            render
            + "RemovedNodeFromSubset("
            + "ID="
            + kgclInstance.id
            + ", "
            + "Subset="
            + kgclInstance.subset
            + ", "
            + "About Node"
            + kgclInstance.about_node
            + ")"
        )

    return render


if __name__ == "__main__":
    app.run(debug=True)
