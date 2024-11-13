from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.order_headers import OrderHeaders
from di_thermax_planmax.ontologies.order_lines import OrderLines
from di_thermax_planmax.view_actions.demo_action import DemoAction
from di_thermax_planmax.view_actions.independent_action import IndependentAction
from di_thermax_planmax.view_actions.inline_order_header_update import InlineOrderHeaderUpdate
from di_thermax_planmax.view_actions.inline_order_line_update import InlineOrderLineUpdate




class DemoChart(Dashboard):
    __dashboard_name__ = "DemoChart"
    __dashboard_description__ = "Demo Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'branch',
                                                         'data': [{'type': 'leaf', 'data': {'views': ['metrics_basic'], 'activeView': 'metrics_basic', 'id': '1'}, 'size': 893},
                                                                  {'type': 'leaf', 'data': {'views': ['metrics_booked_basic'], 'activeView': 'metrics_booked_basic', 'id': '12'},
                                                                   'size': 894.949951171875}], 'size': 185},
                                                        {'type': 'leaf', 'data': {'views': ['table_metrics_basic'], 'activeView': 'table_metrics_basic', 'id': '2'}, 'size': 260,
                                                         'visible': False},
                                                        {'type': 'leaf', 'data': {'views': ['table_metrics_booked_basic'], 'activeView': 'table_metrics_booked_basic', 'id': '4'},
                                                         'size': 260, 'visible': False},
                                                        {'type': 'leaf', 'data': {'views': ['table_booked_order_by_org'], 'activeView': 'table_booked_order_by_org', 'id': '5'},
                                                         'size': 260, 'visible': False},
                                                        {'type': 'leaf', 'data': {'views': ['charts_booked_order_by_curr'], 'activeView': 'charts_booked_order_by_curr', 'id': '6'},
                                                         'size': 260, 'visible': False}, {'type': 'branch', 'data': [
            {'type': 'leaf', 'data': {'views': ['tables_order_header'], 'activeView': 'tables_order_header', 'id': '7'}, 'size': 893},
            {'type': 'leaf', 'data': {'views': ['charts_basic'], 'activeView': 'charts_basic', 'id': '9'}, 'size': 894.949951171875}], 'size': 592.7833251953125},
                                                        {'type': 'leaf', 'data': {'views': ['table_line_details'], 'activeView': 'table_line_details', 'id': '8'}, 'size': 260,
                                                         'visible': False},
                                                        {'type': 'leaf', 'data': {'views': ['tables_all_order_header'], 'activeView': 'tables_all_order_header', 'id': '10'},
                                                         'size': 260, 'visible': False}], 'size': 1787.949951171875}
    __grid_width__ = 1787.949951171875
    __grid_height__ = 777.7833251953125
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 7

    # Basic Metric without any relations only drill down Table

    metrics_basic = PanelComponent(component_type="metrics",
                                   name="Entered Orders",
                                   query="Select(func.count(OrderHeaders.header_id).label('count')).filter(OrderHeaders.flow_status_code == 'ENTERED')",
                                   data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                   header="Entered Orders",
                                   description="Entered Orders",
                                   columns=[],
                                   chart_options={},
                                   content_component="mediator",
                                   relations=[],
                                   details=['table_metrics_basic'])

    table_metrics_basic = PanelComponent(component_type="tables",
                                         name="Entered Order Details",
                                         query="Select(OrderHeaders.organization_code, OrderHeaders.order_type_id, OrderHeaders.order_number, OrderHeaders.version_number).filter(OrderHeaders.flow_status_code == 'ENTERED')",
                                         data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                         header="Entered Order Details",
                                         description="Details of Entered Orders",
                                         columns=[ColumnProperty(column=OrderHeaders.organization_code, display_name="Org Code"),
                                                  ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID", invisible=True),
                                                  ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                                  ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number")],
                                         chart_options={},
                                         content_component="mediator",
                                         relations=[],
                                         inline_actions="InlineOrderHeaderUpdate",
                                         actions=["DemoAction", "IndependentAction"])

    # Metric with Relations and Drill Down Table

    metrics_booked_basic = PanelComponent(component_type="metrics",
                                          name="Booked Orders",
                                          query="Select(func.count(OrderHeaders.header_id).label('count')).filter(OrderHeaders.flow_status_code == 'BOOKED')",
                                          data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                          header="Booked Orders",
                                          description="Booked Orders",
                                          columns=[],
                                          chart_options={},
                                          content_component="mediator",
                                          relations=[{"component_name": "table_booked_order_by_org",
                                                      "relation_name": "Booked Orders by Org",
                                                      "relations": [{"source_class_name": "OeOrderHeadersAll",
                                                                     "source_column_name": "flow_status_code",
                                                                     "source_static_value": "BOOKED",
                                                                     "destination_class_name": "OeOrderHeadersAll",
                                                                     "destination_column_name": "flow_status_code"}]
                                                      },
                                                     {"component_name": "charts_booked_order_by_curr",
                                                      "relation_name": "Booked Orders by Org",
                                                      "relations": [{"source_class_name": "OeOrderHeadersAll",
                                                                     "source_column_name": "flow_status_code",
                                                                     "source_static_value": "BOOKED",
                                                                     "destination_class_name": "OeOrderHeadersAll",
                                                                     "destination_column_name": "flow_status_code"}]
                                                      }
                                                     ],
                                          details=['table_metrics_booked_basic'])

    table_metrics_booked_basic = PanelComponent(component_type="tables",
                                                name="Booked Order Details",
                                                query="Select(OrderHeaders.organization_code, OrderHeaders.order_type_id, OrderHeaders.order_number, OrderHeaders.version_number).filter(OrderHeaders.flow_status_code == 'BOOKED')",
                                                data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                                header="Booked Order Details",
                                                description="Details of Booked Orders",
                                                columns=[ColumnProperty(column=OrderHeaders.organization_code, display_name="Org Code"),
                                                         ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID", invisible=True),
                                                         ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                                         ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number")],
                                                chart_options={},
                                                content_component="mediator",
                                                relations=[],
                                                inline_actions=None,
                                                actions=["DemoAction", "IndependentAction"]
                                                )

    table_booked_order_by_org = PanelComponent(component_type="tables",
                                               name="Booked orders by Org",
                                               query="Select(OrderHeaders.organization_code, func.count(OrderHeaders.order_number).label('Count of Orders')).group_by(OrderHeaders.organization_code)",
                                               data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                               header="Booked orders by Org",
                                               description="Details of Booked orders by Org",
                                               columns=[ColumnProperty(column=OrderHeaders.organization_code, display_name="Org Code"),
                                                        # ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID", invisible=True),
                                                        ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                                        # ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number")
                                                        ],
                                               chart_options={},
                                               content_component="mediator",
                                               relations=[],
                                               inline_actions=None,
                                               actions=["DemoAction", "IndependentAction"]
                                               )

    charts_booked_order_by_curr = PanelComponent(component_type="charts",
                                                 name="Booked Orders by Curr",
                                                 query="Select(OrderHeaders.transactional_curr_code, func.count(OrderHeaders.header_id).label('count')).group_by(OrderHeaders.transactional_curr_code)",
                                                 data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                                 header="Booked Orders by Curr",
                                                 description="Booked Orders by Curr",
                                                 columns=[],
                                                 chart_options={
                                                     "series": [
                                                         {
                                                             "label": {
                                                                 "margin": 8,
                                                                 "show": True
                                                             },
                                                             "name": "Items",
                                                             "type": "bar"
                                                         }
                                                     ],
                                                     "title": [
                                                         {
                                                             "show": True,
                                                             "subtext": "Open orders",
                                                             "text": "Open Jobs by Currency"
                                                         }
                                                     ],
                                                     "tooltip": {
                                                         "show": True
                                                     },
                                                     "xAxis": {
                                                         "type": "category"
                                                     },
                                                     "yAxis": {
                                                     }
                                                 },
                                                 content_component="mediator",
                                                 relations=[])

    # Sample Table with Relations

    tables_order_header = PanelComponent(component_type="tables",
                                         name="Order Header Details",
                                         query="Select(OrderHeaders.header_id, OrderHeaders.organization_code, OrderHeaders.org_id, OrderHeaders.order_type_id, OrderHeaders.order_number, OrderHeaders.version_number).filter(OrderHeaders.flow_status_code == 'BOOKED')",
                                         data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                         header="Order Header Details",
                                         description="Order Header Details",
                                         columns=[
                                             ColumnProperty(column=OrderHeaders.header_id, display_name="Header ID"),
                                             ColumnProperty(column=OrderHeaders.organization_code, display_name="Organization Code"),
                                             ColumnProperty(column=OrderHeaders.org_id, display_name="Org ID"),
                                             ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID"),
                                             ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                             ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number"),
                                         ],
                                         chart_options={},
                                         content_component="mediator",
                                         relations=[{"component_name": "table_line_details",
                                                     "relation_name": "Order Header Line details",
                                                     "relations": [{"source_class_name": "OeOrderHeadersAll",
                                                                    "source_column_name": "header_id",
                                                                    "destination_class_name": "OeOrderLinesAll",
                                                                    "destination_column_name": "header_id"}]
                                                     }],
                                         inline_actions=None,
                                         actions=["DemoAction", "IndependentAction"]
                                         )

    table_line_details = PanelComponent(component_type="tables",
                                        name="Order Line Details",
                                        query="Select(OrderLines.line_id, OrderLines.organization_code, OrderLines.segment1, OrderLines.line_number, OrderLines.ordered_item, OrderLines.header_id)",
                                        data_objects={'OrderLines': 'demo_project.ontologies.order_lines'},
                                        header="Order Line Details",
                                        description="Order Line Details",
                                        columns=[
                                            ColumnProperty(column=OrderLines.line_id, display_name="Line ID"),
                                            ColumnProperty(column=OrderLines.organization_code, display_name="Org Code"),
                                            ColumnProperty(column=OrderLines.segment1, display_name="Item Number"),
                                            ColumnProperty(column=OrderLines.line_number, display_name="Line Number"),
                                            ColumnProperty(column=OrderLines.ordered_item, display_name="Ordered Item"),
                                            ColumnProperty(column=OrderLines.header_id, display_name="Header ID", invisible=True),
                                        ],
                                        chart_options={},
                                        content_component="mediator",
                                        relations=[],
                                        inline_actions="InlineOrderLineUpdate",
                                        actions=["DemoAction", "IndependentAction"]
                                        )

    # Charts Dill down and relations
    charts_basic = PanelComponent(component_type="charts",
                                  name="Orders By Status",
                                  query="Select(OrderHeaders.flow_status_code, func.count(OrderHeaders.header_id).label('count')).group_by(OrderHeaders.flow_status_code)",
                                  data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                  header="Orders By Status",
                                  description="Orders By Status",
                                  columns=[],
                                  chart_options={
                                      "series": [
                                          {
                                              "label": {
                                                  "margin": 8,
                                                  "show": True
                                              },
                                              "name": "Items",
                                              "type": "bar",
                                              "encode": {"x": 'flow_status_code', "y": 'count'},
                                          }
                                      ],
                                      "title": [
                                          {
                                              "show": True,
                                              "subtext": "Order Details",
                                              "text": "Order Details by Status"
                                          }
                                      ],
                                      "tooltip": {
                                          "show": True
                                      },
                                      "xAxis": {
                                          "type": "category"
                                      },
                                      "yAxis": {
                                      }
                                  },
                                  content_component="mediator",
                                  relations=[{"component_name": "tables_all_order_header",
                                              "relation_name": "Order Status Details",
                                              "relations": [{"source_class_name": "OeOrderHeadersAll",
                                                             "source_column_name": "flow_status_code",
                                                             "destination_class_name": "OeOrderHeadersAll",
                                                             "destination_column_name": "flow_status_code"}]
                                              }],
                                  drill_downs={0: "OrderHeaders.transactional_curr_code",
                                               1: "OrderHeaders.shipping_method_code"}
                                  )

    tables_all_order_header = PanelComponent(component_type="tables",
                                             name="Order Header Details",
                                             query="Select(OrderHeaders.header_id, OrderHeaders.organization_code, OrderHeaders.org_id, OrderHeaders.order_type_id, OrderHeaders.order_number, OrderHeaders.version_number)",
                                             data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                             header="Order Header Details",
                                             description="Order Header Details",
                                             columns=[
                                                 ColumnProperty(column=OrderHeaders.header_id, display_name="Header ID"),
                                                 ColumnProperty(column=OrderHeaders.organization_code, display_name="Organization Code"),
                                                 ColumnProperty(column=OrderHeaders.org_id, display_name="Org ID"),
                                                 ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID"),
                                                 ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                                 ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number"),
                                             ],
                                             chart_options={},
                                             content_component="mediator",
                                             relations=[],
                                             inline_actions=None,
                                             actions=["DemoAction", "IndependentAction"]
                                             )
