Name:		texlive-penlight
Version:	72301
Release:	1
Summary:	Penlight Lua libraries made available to LuaLaTeX users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/penlight
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/penlight.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/penlight.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LuaLaTeX package provides a wrapper to use the penlight
Lua libraries with LuaLaTeX, with some extra functionality
added.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/penlight
%doc %{_texmfdistdir}/doc/luatex/penlight

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
