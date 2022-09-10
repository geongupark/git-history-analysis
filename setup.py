# python setup.py command | New command
# python setup.py sdist   | python - m build
# python setup.py test	   | pytest
# python setup.py install | pip install
# python setup.py develop | pip install - e
# python setup.py bdist_wheel
from setuptools import setup


def main() -> None:
    with open("requirements.txt") as fp:
        install_requires = fp.read().strip().split("\n")

    metadata = dict(
        install_requires=install_requires
    )
    setup(**metadata)


if __name__ == "__main__":
    main()
