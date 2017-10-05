load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_library")

# TODO(murt): Migrate these to builtin cc_proto_library and py_proto_library once the well known
# proto types rule is added to bazelbuild https://github.com/google/protobuf/issues/2763

filegroup(
    name = "protos",
    srcs = [
        "google/api/annotations.proto",
        "google/api/http.proto",
    ],
    visibility = ["//visibility:public"],
)

# NOTE: The *_proto_library rules do not correctly handle deps, so we have to add all dependent
# proto files as inputs. See: https://github.com/pubref/rules_protobuf/issues/130
# TODO(kgreenek): Just use deps once that bug is fixed.
PROTO_IMPORTS = [
    "external/com_google_protobuf/src/",
    "external/googleapis_archive",
]
PROTO_INPUTS = ["@com_google_protobuf//:well_known_protos"]

py_proto_library(
    name = "py_proto",
    imports = PROTO_IMPORTS,
    inputs = PROTO_INPUTS,
    protos = [":protos"],
    visibility = ["//visibility:public"],
)
