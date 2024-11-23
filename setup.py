import setuptools

class BinaryDistribution(setuptools.dist.Distribution):
  def has_ext_modules(foo):
    return True

setuptools.setup(
  name="pyturn",
  packages=setuptools.find_packages(include=["pyturn"]),
  py_modules = ["pyturn._turn"],
  package_data={"pyturn": ["*.so", "*.pyd"]},
  include_package_data=True,
  distclass=BinaryDistribution, # Comment this line out if compiling for a different architechture
)
