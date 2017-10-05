http_archive(
    name = "io_bazel_rules_python",
    sha256 = "1210df6ec5355ab4eeb5b79cdde7cdb77b0432fd8e9ab1744abe7ac5ef4b2c78",
    strip_prefix = "rules_python-44fdf5f24a4b634ef7b0f86e7a017f4d8d5aa899",
    urls = ["https://github.com/bazelbuild/rules_python/archive/44fdf5f24a4b634ef7b0f86e7a017f4d8d5aa899.tar.gz"],
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

pip_import(
   name = "pip_requirements",
   requirements = "//:requirements.txt",
)

load("@pip_requirements//:requirements.bzl", "pip_install")

pip_install()

git_repository(
    name = "org_pubref_rules_protobuf",
    commit = "ff3b7e7963daa7cb3b42f8936bc11eda4b960926",  # October 3, 2017
    remote = "https://github.com/pubref/rules_protobuf.git",
)

load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_repositories")

py_proto_repositories()

new_http_archive(
    name = "googleapis_archive",
    build_file = "//third_party:googleapis.BUILD",
    sha256 = "df585427959ebb9949ca12a45888b50a5b8edcb2b270aea1800225d159a49ff6",
    strip_prefix = "googleapis-3273178ea4684acc4f512f7bef7349dd72db88f6",
    urls = ["https://github.com/googleapis/googleapis/archive/3273178ea4684acc4f512f7bef7349dd72db88f6.tar.gz"],
)

bind(
    name = "googleapis_protos",
    actual = "@googleapis_archive//:protos",
)

bind(
    name = "googleapis_py_proto",
    actual = "@googleapis_archive//:py_proto",
)
