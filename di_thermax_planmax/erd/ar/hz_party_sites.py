from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.hz_cust_acct_sites_all import HzCustAcctSitesAll
    from ..ar.hz_locations import HzLocations
    from ..ar.hz_parties import HzParties


class HzPartySites(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hz_party_sites"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 2238.5342712402344, "ui_y_pos": 1475.9617919921875, "colour": "#F2F3F5"}

    party_site_id: Mapped[str] = mapped_column('party_site_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    party_id: Mapped[str] = mapped_column('party_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location_id: Mapped[str] = mapped_column('location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_site_number: Mapped[str] = mapped_column('party_site_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wh_update_date: Mapped[str] = mapped_column('wh_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute_category: Mapped[str] = mapped_column('attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column('attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column('attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column('attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column('attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column('attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column('attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute7: Mapped[str] = mapped_column('attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute8: Mapped[str] = mapped_column('attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute9: Mapped[str] = mapped_column('attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute10: Mapped[str] = mapped_column('attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute16: Mapped[str] = mapped_column('attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column('attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column('attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column('attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column('attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute1: Mapped[str] = mapped_column('global_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute2: Mapped[str] = mapped_column('global_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute3: Mapped[str] = mapped_column('global_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute4: Mapped[str] = mapped_column('global_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute5: Mapped[str] = mapped_column('global_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute6: Mapped[str] = mapped_column('global_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute7: Mapped[str] = mapped_column('global_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute8: Mapped[str] = mapped_column('global_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute9: Mapped[str] = mapped_column('global_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute10: Mapped[str] = mapped_column('global_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute11: Mapped[str] = mapped_column('global_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute12: Mapped[str] = mapped_column('global_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute13: Mapped[str] = mapped_column('global_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute14: Mapped[str] = mapped_column('global_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute15: Mapped[str] = mapped_column('global_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute16: Mapped[str] = mapped_column('global_attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute17: Mapped[str] = mapped_column('global_attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute18: Mapped[str] = mapped_column('global_attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute19: Mapped[str] = mapped_column('global_attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute20: Mapped[str] = mapped_column('global_attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_system_reference: Mapped[str] = mapped_column('orig_system_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date_active: Mapped[str] = mapped_column('start_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_date_active: Mapped[str] = mapped_column('end_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    region: Mapped[str] = mapped_column('region', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mailstop: Mapped[str] = mapped_column('mailstop', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_key_osm: Mapped[str] = mapped_column('customer_key_osm', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    phone_key_osm: Mapped[str] = mapped_column('phone_key_osm', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contact_key_osm: Mapped[str] = mapped_column('contact_key_osm', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    identifying_address_flag: Mapped[str] = mapped_column('identifying_address_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    language: Mapped[str] = mapped_column('language', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column('status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_site_name: Mapped[str] = mapped_column('party_site_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    addressee: Mapped[str] = mapped_column('addressee', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_module: Mapped[str] = mapped_column('created_by_module', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    application_id: Mapped[str] = mapped_column('application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_content_source: Mapped[str] = mapped_column('actual_content_source', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_location_number: Mapped[str] = mapped_column('global_location_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    duns_number_c: Mapped[str] = mapped_column('duns_number_c', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    HzCustAcctSitesAll_party_site_id: Mapped["HzCustAcctSitesAll"] = relationship(back_populates="HzPartySites_party_site_id", primaryjoin="HzCustAcctSitesAll.party_site_id==HzPartySites.party_site_id", foreign_keys="[HzCustAcctSitesAll.party_site_id]", viewonly=True)
        

    

    HzLocations_location_id: Mapped["HzLocations"] = relationship(back_populates="HzPartySites_location_id", primaryjoin="HzLocations.location_id==HzPartySites.location_id", foreign_keys="[HzLocations.location_id]", viewonly=True)
        

    

    HzParties_party_id: Mapped["HzParties"] = relationship(back_populates="HzPartySites_party_id", primaryjoin="HzParties.party_id==HzPartySites.party_id", foreign_keys="[HzPartySites.party_id]", viewonly=True)



