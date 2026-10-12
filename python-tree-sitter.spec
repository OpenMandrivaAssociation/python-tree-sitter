Name:		python-tree-sitter
Version:	0.26.0
Release:	1
Summary:	Python bindings to the Tree-sitter parsing library
License:	MIT
Group:		Development/Python
URL:		https://github.com/tree-sitter/py-tree-sitter
Source0:	https://files.pythonhosted.org/packages/source/t/tree-sitter/tree-sitter-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang

%description
Python bindings for Tree-sitter. Used by Aider's repo-map (grep-ast).

%prep
%autosetup -n tree-sitter-%{version}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter
%{python_sitearch}/tree_sitter-*.*-info
