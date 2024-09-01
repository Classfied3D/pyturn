import setuptools

setuptools.setup(
  name="py",
  packages=setuptools.find_packages(include=["pyturn"]),
  py_modules = ["pyturn.turn"],
  package_data={"pyturn": ["*.so"]},
  include_package_data=True,
)