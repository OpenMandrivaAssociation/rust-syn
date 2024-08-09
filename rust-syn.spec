# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# check dependencies break bootstrapping
%bcond_with check
%global debug_package %{nil}

%global crate syn

Name:           rust-syn
Version:        2.0.72
Release:        1
Summary:        Parser for Rust source code
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/syn
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(proc-macro2) >= 1.0.83 with crate(proc-macro2) < 2.0.0~)
BuildRequires:  (crate(proc-macro2/proc-macro) >= 1.0.83 with crate(proc-macro2/proc-macro) < 2.0.0~)
BuildRequires:  (crate(quote) >= 1.0.35 with crate(quote) < 2.0.0~)
BuildRequires:  (crate(quote/proc-macro) >= 1.0.35 with crate(quote/proc-macro) < 2.0.0~)
BuildRequires:  (crate(unicode-ident/default) >= 1.0.0 with crate(unicode-ident/default) < 2.0.0~)
BuildRequires:  rust >= 1.61
%if %{with check}
BuildRequires:  (crate(anyhow/default) >= 1.0.0 with crate(anyhow/default) < 2.0.0~)
BuildRequires:  (crate(automod/default) >= 1.0.0 with crate(automod/default) < 2.0.0~)
BuildRequires:  (crate(flate2/default) >= 1.0.0 with crate(flate2/default) < 2.0.0~)
BuildRequires:  (crate(insta/default) >= 1.0.0 with crate(insta/default) < 2.0.0~)
BuildRequires:  (crate(rayon/default) >= 1.0.0 with crate(rayon/default) < 2.0.0~)
BuildRequires:  (crate(ref-cast/default) >= 1.0.0 with crate(ref-cast/default) < 2.0.0~)
BuildRequires:  (crate(reqwest/blocking) >= 0.12.0 with crate(reqwest/blocking) < 0.13.0~)
BuildRequires:  (crate(reqwest/default) >= 0.12.0 with crate(reqwest/default) < 0.13.0~)
BuildRequires:  (crate(rustversion/default) >= 1.0.0 with crate(rustversion/default) < 2.0.0~)
BuildRequires:  (crate(syn-test-suite/default) >= 0.0.0 with crate(syn-test-suite/default) < 1.0.0~)
BuildRequires:  (crate(tar/default) >= 0.4.16 with crate(tar/default) < 0.5.0~)
BuildRequires:  (crate(termcolor/default) >= 1.0.0 with crate(termcolor/default) < 2.0.0~)
BuildRequires:  (crate(walkdir/default) >= 2.3.2 with crate(walkdir/default) < 3.0.0~)
%endif

%global _description %{expand:
Parser for Rust source code.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn) = 2.0.72
Requires:       (crate(proc-macro2) >= 1.0.83 with crate(proc-macro2) < 2.0.0~)
Requires:       (crate(unicode-ident/default) >= 1.0.0 with crate(unicode-ident/default) < 2.0.0~)
Requires:       cargo
Requires:       rust >= 1.61

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/default) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72
Requires:       crate(syn/clone-impls) = 2.0.72
Requires:       crate(syn/derive) = 2.0.72
Requires:       crate(syn/parsing) = 2.0.72
Requires:       crate(syn/printing) = 2.0.72
Requires:       crate(syn/proc-macro) = 2.0.72

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clone-impls-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/clone-impls) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+clone-impls-devel %{_description}

This package contains library source intended for building other packages which
use the "clone-impls" feature of the "%{crate}" crate.

%files       -n %{name}+clone-impls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/derive) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+extra-traits-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/extra-traits) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+extra-traits-devel %{_description}

This package contains library source intended for building other packages which
use the "extra-traits" feature of the "%{crate}" crate.

%files       -n %{name}+extra-traits-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fold-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/fold) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+fold-devel %{_description}

This package contains library source intended for building other packages which
use the "fold" feature of the "%{crate}" crate.

%files       -n %{name}+fold-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/full) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parsing-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/parsing) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+parsing-devel %{_description}

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%files       -n %{name}+parsing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+printing-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/printing) = 2.0.72
Requires:       (crate(quote) >= 1.0.35 with crate(quote) < 2.0.0~)
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+printing-devel %{_description}

This package contains library source intended for building other packages which
use the "printing" feature of the "%{crate}" crate.

%files       -n %{name}+printing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/proc-macro) = 2.0.72
Requires:       (crate(proc-macro2/proc-macro) >= 1.0.83 with crate(proc-macro2/proc-macro) < 2.0.0~)
Requires:       (crate(quote) >= 1.0.35 with crate(quote) < 2.0.0~)
Requires:       (crate(quote/proc-macro) >= 1.0.35 with crate(quote/proc-macro) < 2.0.0~)
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/test) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+visit-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/visit) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+visit-devel %{_description}

This package contains library source intended for building other packages which
use the "visit" feature of the "%{crate}" crate.

%files       -n %{name}+visit-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+visit-mut-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(syn/visit-mut) = 2.0.72
Requires:       cargo
Requires:       crate(syn) = 2.0.72

%description -n %{name}+visit-mut-devel %{_description}

This package contains library source intended for building other packages which
use the "visit-mut" feature of the "%{crate}" crate.

%files       -n %{name}+visit-mut-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
