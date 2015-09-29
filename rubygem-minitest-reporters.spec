#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-minitest-reporters
Version  : 1.0.17
Release  : 4
URL      : https://rubygems.org/downloads/minitest-reporters-1.0.17.gem
Source0  : https://rubygems.org/downloads/minitest-reporters-1.0.17.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-ansi
BuildRequires : rubygem-builder
BuildRequires : rubygem-bundler
BuildRequires : rubygem-maruku
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-ruby-progressbar
BuildRequires : rubygem-rubygems-tasks

%description
[gem]: https://rubygems.org/gems/minitest-reporters
[travis]: https://travis-ci.org/rom-rb/rom-mongo

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n minitest-reporters-1.0.17
gem spec %{SOURCE0} -l --ruby > rubygem-minitest-reporters.gemspec

%build
gem build rubygem-minitest-reporters.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
minitest-reporters-1.0.17.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/minitest-reporters-1.0.17 && rake test --trace && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/minitest-reporters-1.0.17.gem
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/Testing/SetupAndTeardown/ForMiniTest/after_teardown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/Testing/SetupAndTeardown/ForMiniTest/before_setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/Testing/SetupAndTeardown/ForMiniTest/cdesc-ForMiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/Testing/SetupAndTeardown/cdesc-SetupAndTeardown.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/Testing/cdesc-Testing.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/ActiveSupport/cdesc-ActiveSupport.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/add_filter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/cdesc-ExtensibleBacktraceFilter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/default_filter-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/filter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/filters%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/ExtensibleBacktraceFilter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/RelativePosition/cdesc-RelativePosition.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/RelativePosition/pad-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/RelativePosition/pad_mark-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/RelativePosition/pad_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/RelativePosition/print_with_info_padding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ANSI/Code/black-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ANSI/Code/cdesc-Code.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ANSI/Code/color%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ANSI/cdesc-ANSI.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/add_defaults-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/after_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/after_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/before_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/before_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/cdesc-BaseReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/filter_backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/print_colored_status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/print_info-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/puts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/total_count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/BaseReporter/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/after_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/before_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/before_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/cdesc-DefaultReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/color%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/colored_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/green-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/message_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/print_failure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/record_failure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/record_pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/record_skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/red-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/result_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/suite_duration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/suite_result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/DefaultReporter/yellow-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/analyze_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/cdesc-JUnitReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/filename_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/message_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/JUnitReporter/xml_message_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/cdesc-ProgressReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/color%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/print_test_with_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/show-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/ProgressReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMateReporter/cdesc-RubyMateReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMateReporter/print_test_with_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMateReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMateReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMateReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/after_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/before_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/before_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/cdesc-RubyMineReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/minitest_test_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/RubyMineReporter/with_result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/after_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/before_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/cdesc-SpecReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/SpecReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/cdesc-Reporters.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/choose_reporters-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/reporters-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/run_with_hooks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/use%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/use_around_test_hooks%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/use_old_activesupport_fix%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/Reporters/use_runner%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/cdesc-Minitest.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/guard_reporter-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/plugin_minitest_reporter_init-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/Minitest/total_count-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-reporters-1.0.17/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/.ruby-gemset
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/Gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/README.md
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/assets/default-reporter.png
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/assets/progress-reporter.png
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/assets/spec-reporter.png
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/extensible_backtrace_filter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/minitest_reporter_plugin.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/old_activesupport_fix.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/relative_position.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/ansi.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/base_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/default_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/junit_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/progress_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/ruby_mate_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/rubymine_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/spec_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/lib/minitest/reporters/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/minitest-reporters.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/fixtures/junit_filename_bug_example_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/fixtures/progress_detailed_skip_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/fixtures/progress_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/fixtures/sample_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/gallery/bad_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/gallery/good_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/integration/reporters/junit_reporter_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/integration/reporters/progress_reporter_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/reports/TEST-something-other.xml
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/unit/minitest/extensible_backtrace_filter_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/unit/minitest/reporters_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-reporters-1.0.17/test/unit/minitest/spec_reporter_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/minitest-reporters-1.0.17.gemspec
