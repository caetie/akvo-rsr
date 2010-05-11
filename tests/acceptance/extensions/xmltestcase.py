# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

# XMLTestCase extends unittest.TestCase to add convenience methods for common assertion patterns

from unittest import TestCase

from helpers.constraintmatchers import *

class XMLTestCase(TestCase):

    def assert_element(self, element):
        self._actual_element = element
        return self

    def is_not_none(self):
        self.failUnless(self._actual_element, "Expected an element -- received None instead")

    def has_single_children_in_list(self, expected_child_tags):
        for expected_tag in expected_child_tags:
            self.has_exactly(1).child_with_tag(expected_tag)

    def has_exactly(self, exactly):
        self._matcher = ExactMatcher(self, exactly)
        return self

    def has_at_least(self, at_least):
        self._matcher = AtLeastMatcher(self, at_least)
        return self

    def children(self):
        self._matcher.set_description("child elements")
        self._matcher.evaluate(len(self._actual_element.getchildren()))

    def children_with_tag(self, expected_tag):
        self._describe_and_evaluate_children_with_tag("children", expected_tag)

    def child_with_tag(self, expected_tag):
        self._describe_and_evaluate_children_with_tag("child", expected_tag)

    def _describe_and_evaluate_children_with_tag(self, child_or_children, expected_tag):
        self._matcher.set_description("%s with tag <%s>" % (child_or_children, expected_tag))
        self._matcher.evaluate(len(self._actual_element.findall(expected_tag)))