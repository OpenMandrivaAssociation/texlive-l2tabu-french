# revision 15878
# category Package
# catalog-ctan /info/l2tabu/french
# catalog-date 2006-12-15 14:14:43 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-l2tabu-french
Version:	20061215
Release:	1
Summary:	French translation of l2tabu
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
French translation of l2tabu.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/README
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/l2tabufr-heavy.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/l2tabufr-light.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/l2tabufr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
