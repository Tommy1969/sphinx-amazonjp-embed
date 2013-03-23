#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst

from . import url


class amazonjp(nodes.General, nodes.Element):
    pass



PRE_TAG = '<iframe src="http://rcm-jp.amazon.co.jp/e/cm?'
POST_TAG = '" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>'



def visit(self, node):

    affiliate_id = self.builder.config.amazonjp_affiliate_id

    query = url.build_query(node.url, affiliate_id, node.options)

    print PRE_TAG + query + POST_TAG

    self.body.append(PRE_TAG + query + POST_TAG)



def depart(self, node):
    pass



class AmazonJPDirective(rst.Directive):

    name = 'amazonjp'
    node_class = amazonjp

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'same_window': rst.directives.flag,
        'hide_border': rst.directives.flag,
        'small': rst.directives.flag
        }


    def run(self):

        node = self.node_class()

        node.url = self.arguments[0]

        node.options = self.options

        return [node]

