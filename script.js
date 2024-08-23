document.addEventListener('DOMContentLoaded', () => {
    const collegeDropdown = document.getElementById('college-dropdown');
    const servicesDropdown = document.getElementById('services-dropdown');
    const confirmBtn = document.getElementById('confirm-btn');
    const outputArea = document.querySelector('.output-area');
  
    // Data mapping
    const messages = {
        'cuny-baruch': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'NYC Department of Homeless Services',
              address: '33 Beaver St, New York, NY 10004',
              phone: '212-361-6000',
              distance: '0.9 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Win NYC',
              address: '115 E 31st St, New York, NY 10016',
              phone: '212-695-6000',
              distance: '1.0 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-staten': {
          'food': [
            {
              name: 'Staten Island Food Pantry',
              address: '120 Anderson Ave, Staten Island, NY 10303',
              phone: '718-273-2525',
              distance: '1.2 mi',
              recommended: 'Yes'
            },
            {
              name: 'St. Peter’s Soup Kitchen',
              address: '53 St. Marks Pl, Staten Island, NY 10301',
              phone: '718-447-3500',
              distance: '2.0 mi',
              recommended: 'No'
            },
            {
              name: 'Richmond Senior Center',
              address: '129 Stuyvesant Pl, Staten Island, NY 10301',
              phone: '718-720-2600',
              distance: '1.8 mi',
              recommended: 'Yes'
            },
            {
              name: 'Project Hospitality',
              address: '100 Park Ave, Staten Island, NY 10302',
              phone: '718-273-3400',
              distance: '2.1 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Community Health Center',
              address: '215 Bay St, Staten Island, NY 10301',
              phone: '718-448-4440',
              distance: '1.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Haven',
              address: '111 W 5th St, Staten Island, NY 10301',
              phone: '718-420-3030',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'Homeless Outreach Program',
              address: '432 Richmond Ave, Staten Island, NY 10312',
              phone: '718-356-1200',
              distance: '2.3 mi',
              recommended: 'Yes'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.0 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-craig': {
          'food': [
            {
              name: 'New York City Food Bank',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.3 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Win NYC',
              address: '115 E 31st St, New York, NY 10016',
              phone: '212-695-6000',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Shelter of Hope',
              address: '88 3rd Ave, New York, NY 10003',
              phone: '212-213-6070',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-health': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-law': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-guttman': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-brooklyn': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-city': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-hunter': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-john-jay': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-queens': {
          'food': [
            {
              name: 'Queens Community House',
              address: '108-25 62nd Dr, Forest Hills, NY 11375',
              phone: '718-592-5757',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '5.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '6.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '6.2 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Homeless Outreach Program',
              address: '122-02 82nd Ave, Kew Gardens, NY 11415',
              phone: '718-830-0973',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'NYC Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '5.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '6.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '6.3 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-york': {
          'food': [
            {
              name: 'York College Food Pantry',
              address: '94-20 Guy R Brewer Blvd, Jamaica, NY 11451',
              phone: '718-262-2000',
              distance: '1.2 mi',
              recommended: 'Yes'
            },
            {
              name: 'Queens Community House',
              address: '108-25 62nd Dr, Forest Hills, NY 11375',
              phone: '718-592-5757',
              distance: '3.0 mi',
              recommended: 'No'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '5.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.8 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Homeless Outreach Program',
              address: '122-02 82nd Ave, Kew Gardens, NY 11415',
              phone: '718-830-0973',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'NYC Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '5.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.8 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '6.0 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-medgar-evers': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.8 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '2.2 mi',
              recommended: 'No'
            }
          ]
        }
      };
  
    function updateOutput(college, service) {
      outputArea.innerHTML = '';
      if (messages[college] && messages[college][service]) {
        const list = document.createElement('ul');
        
        messages[college][service].forEach((entry) => {
          const listItem = document.createElement('li');
          
          const content = `
            <strong>${entry.name}</strong><br>
            <ul>
              <li><strong>Address:</strong> ${entry.address}</li>
              <li><strong>Phone:</strong> ${entry.phone}</li>
              <li><strong>Distance:</strong> ${entry.distance}</li>
              <li><strong>Recommended by CUNY:</strong> ${entry.recommended}</li>
            </ul>
          `;
          
          listItem.innerHTML = content;
          list.appendChild(listItem);
        });
  
        outputArea.appendChild(list);
      } else {
        outputArea.textContent = 'No information available for this selection.';
      }
    }
  
    confirmBtn.addEventListener('click', () => {
      const selectedCollege = collegeDropdown.value;
      const selectedService = servicesDropdown.value;
      updateOutput(selectedCollege, selectedService);
    });
  });
  