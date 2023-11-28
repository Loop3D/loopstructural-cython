from setuptools import Extension, setup
import numpy

setup(
    ext_modules=[
        Extension(
            name="loopstructuralcython.cg",  # as it would be imported
            # may include packages/namespaces separated by `.`
            sources=[
                "loopstructuralcython\loopstructuralcython\cg.pyx"
            ],  # all sources are compiled into a single binary file
        ),
    ],
    include_dirs=[numpy.get_include()],
)
