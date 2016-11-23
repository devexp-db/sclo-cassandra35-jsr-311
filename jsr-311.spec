%{?scl:%scl_package jsr-311}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jsr-311
Version:	1.1.1
Release:	13%{?dist}
Summary:	JAX-RS: Java API for RESTful Web Services
License:	CDDL
URL:		http://jsr311.java.net
# svn export https://svn.java.net/svn/jsr311~svn/tags/jsr311-api-1.1.1 jsr-311-1.1.1
# tar cvzf jsr-311-1.1.1.tgz jsr-311-1.1.1
Source0:	%{pkg_name}-%{version}.tgz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_java_common}junit
%{?scl:Requires: %scl_runtime}

Provides:	javax.ws.rs
BuildArch:	noarch

%description
JAX-RS: Java API for RESTful Web Services

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "///pom:extensions/pom:extension[pom:artifactId='wagon-svn']"
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file :jsr311-api %{pkg_name} javax.ws.rs/%{pkg_name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_javadir}/javax.ws.rs/

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 23 2016 Tomas Repik <trepik@redhat.com> - 1.1.1-13
- scl conversion

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Michal Srb <msrb@redhat.com> - 1.1.1-11
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1.1-8
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.1-7
- Add javax.ws.rs provides and directory

* Mon Aug 05 2013 gil cattaneo <puntogil@libero.it> 1.1.1-6
- rebuilt rhbz#992645
- swith to Xmvn
- adapt to new guideline

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2011 Juan Hernandez <juan.hernandez@redhat.com> 1.1.1-1
- Adapted (mostly copied, in fact) from the corresponding package from Mageia
  (http://www.mageia.org) with support from Gil Cattaneo <puntogil@libero.it>.
