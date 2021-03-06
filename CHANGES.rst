Changelog
=========

1.2 (unreleased)
----------------

- Contact details of a person fallbacks to person's main position
  get from IPersonHeldPositions adapter.
  [thomasdesvenain]

- Added an IPersonHeldPositions adapter that gets positions sorted by status :
  a main position, all current positions, closed positions.
  [thomasdesvenain]

- Sort get_held_positions on organization.
  [cedricmessiant]

- Add plone.abovecontenttitle viewlet manager to person, organization, position
  and contact (held_position) views.
  [vincentfretin]

- js functions have a namespace.
  [thomasdesvenain]

- Add an api to make dependencies between a contact field and an other one.
  (needs collective.contact.widget >= 1.2)
  [thomasdesvenain]

- Add parameter to choose if we want to display person title in person's displayed title.
  [cedricmessiant]

- Tools for excel export with collective.excelexport:
  - renderer for contact field,
  - exportable to show person infos on held_position export.
  [thomasdesvenain]


1.1 (2014-03-11)
----------------

- Remove meta_type override because it breaks copy support.
  [thomasdesvenain]

- Fix if for any reason use_parent_address is True, content has an address and
  has no parent with an address.
  [thomasdesvenain]

- Add help messages on add contact form.
  [thomasdesvenain]

- Display more information about "other contacts" in organization view.
  [cedricmessiant]

- Add ICustomSettings adapter lookup in widget settings utility to be
  able to overrides add_url_for_portal_type method in some projects.
  [vincentfretin]

- Rewrite every contact content view in separate views (basefields, contactdetails, etc) so
  that we can override only a specific part of the view in customer projects.
  [cedricmessiant]

- Rename all contact content views to "view".
  [cedricmessiant]

- Add hcard microformat (see http://microformats.org/wiki/hcard) for person and organization.
  [cedricmessiant]

- Use a macro to display contact details.
  [thomasdesvenain]

- Manage case users have uploaded non-image formats for logo or photo.
  [thomasdesvenain]

- Display behavior fields on contactable views
  once they are in default fieldset.
  [thomasdesvenain]

- Fixed: keep order of TTW fields displayed on view pages.
  [thomasdesvenain]

- Add tooltip overviews for held positions, persons, positions and organizations.
  [cedricmessiant]

- Use thumb scale for logos and photos.
  [cedricmessiant]

- Add icon for 'Create Contact' link on position and organization pages.
  [cedricmessiant]

- Customize sortable_title indexer for Person and Held Position
  and add a corresponding brain
  metadata (to enable use of this index in collective.contact.facetednav
  alphabetic search widget).
  [cedricmessiant]

- A content that just implements IContactDetails behavior
  is adaptatable to IContactable and have a VCal export.
  [thomasdesvenain]

- We can hide Use parent address field using a permission:
  "collective.contact.core.UseParentAddress"
  So it is possible to remove this feature via rolemap
  or remove it on some content types via workflow.
  [thomasdesvenain]

- Don't crash when deleting position or organization if a held position is
  associated with it. Show relations that will be broken
  (plone.app.linkintegrity integration).
  [vincentfretin]

- Fix ObjectModifiedEvent subscribers to not reindex if event is
  a ContainerModifiedEvent.
  [vincentfretin]

- Don't show use_parent_address checkbox if there is no parent address.
  [cedricmessiant]

- Fix parent address in add forms.
  [cedricmessiant]

- Add more robot framework tests.
  [cedricmessiant]

- Add 'Create Contact' link on position view.
  [cedricmessiant]

- Use full title instead of Title in position view title.
  [cedricmessiant]

- Show organization's and root organization's name in position's full title.
  [cedricmessiant]

- Add first organization title in held position's title.
  [cedricmessiant]

- Added logo and activity rich field on organization type.
  [thomasdesvenain]

- Fixed generate id from title on held positions and persons.
  [thomasdesvenain]

- When we get the address of a contact, if the most direct address is empty,
  look for the next.
  [thomasdesvenain]

- Added Fax and Website fields to IContactDetails and IContactable.
  [thomasdesvenain]

- Fixed javascript in @@add-organization view.
  [vincentfretin]

- Fixed use parent address if we set Contact Details behaviour on held positions.
  [thomasdesvenain]

- Add vCard support to organizations
  [ebrehault]

1.0 (2013-09-13)
----------------

- Birthday is now optional as a behaviour.
  [thomasdesvenain]

- Use (-200, 1) years range for birthday field.
  [vincentfretin]

- "Add new" popup link is renamed from "Add ..." to "Create ..."
  [thomasdesvenain]

- New behaviour to add a "Related organizations" field on a content type.
  [thomasdesvenain]

- Plain text search improvements :
    - we can find persons with organization names, functions names,
    - the same for held positions,
    - indexation is updated when organization or function changes
  [thomasdesvenain]

- Messages that document better the organization / position held position
  adding process.
  [thomasdesvenain]

- Display position label in title of held position view page.
  [thomasdesvenain]

- Added an additional input text label to held positions,
  used on titles if held_position is directly related to an organization.
  [thomasdesvenain]

- Display contacts on organization page.
  [thomasdesvenain]

- We can find a function with the organization name.
  [thomasdesvenain]

- Fixed field customization view.
  [vincentfretin, thomasdesvenain]

- Fixed held_position field showing in Add contact overlay if Plone site id
  is different of Plone.
  [vincentfretin]

- Added workflows for contact objects.
  [cedricmessiant]


0.11 (2013-03-11)
-----------------

- Fixed bug with default views.
  [cedricmessiant]


0.10 (2013-03-07)
-----------------

- Fixed MANIFEST.in
  [cedricmessiant]


0.9 (2013-03-07)
----------------

- Initial release
  [cedricmessiant]

