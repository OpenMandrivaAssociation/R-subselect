%global packname  subselect
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.11_3
Release:          1
Summary:          Selecting variable subsets
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.11-3.tar.gz
Requires:         R-MASS R-ISwR 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-MASS R-ISwR 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
A collection of functions which (i) assess the quality of variable subsets
as surrogates for a full data set, in either an exploratory data analysis
or in the context of a multivariate linear model, and (ii) search for
subsets which are optimal under various criteria.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/readme
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
